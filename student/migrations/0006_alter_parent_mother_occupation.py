# Generated by Django 5.1.3 on 2024-11-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_parent_mother_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='mother_occupation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
