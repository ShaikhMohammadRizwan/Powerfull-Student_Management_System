# Generated by Django 5.1.3 on 2024-11-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='PwaY8ELfqQeR80PRgRLqcaUHW0fv58uT', editable=False, max_length=32, unique=True),
        ),
    ]
