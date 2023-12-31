from django.db import models
from django.contrib.auth.models import AbstractUser, Group, BaseUserManager, Permission, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, staff_id, password=None, **extra_fields):
        if not staff_id:
            raise ValueError('The Staff ID must be set')
        user = self.model(staff_id=staff_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staff_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(staff_id, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
    staff_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)


    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups'
    )

    user_permissions = models.ManyToManyField(Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_user_permissions'
    )

    USERNAME_FIELD = 'staff_id'

    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.name