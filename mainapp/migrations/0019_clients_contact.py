# Generated by Django 4.1 on 2024-01-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0018_delete_about_delete_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="clients",
            name="contact",
            field=models.CharField(default="020", max_length=50),
        ),
    ]
