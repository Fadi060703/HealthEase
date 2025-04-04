# Generated by Django 5.1.7 on 2025-03-23 09:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_language_nationality_doctorprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='nationalities',
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='doc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doc_profile_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('languages', models.ManyToManyField(to='app.language')),
                ('nationalities', models.ManyToManyField(to='app.nationality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='userprofile_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.userprofile'),
            preserve_default=False,
        ),
    ]
