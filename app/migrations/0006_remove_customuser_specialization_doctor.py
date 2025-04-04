# Generated by Django 5.1.1 on 2025-03-12 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_speicalization_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='specialization',
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec', to='app.speicalization')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('app.customuser',),
        ),
    ]
