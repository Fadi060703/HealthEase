# Generated by Django 5.1.7 on 2025-03-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_doctorprofile_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='profile_images/'),
            preserve_default=False,
        ),
    ]
