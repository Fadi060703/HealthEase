# Generated by Django 5.1.1 on 2025-03-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer Not To Say'), ('E', 'Rami Asfoura')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
