# Generated by Django 5.1.1 on 2025-03-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customuser_username'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_groups', to='auth.group'),
        ),
    ]
