# Generated by Django 5.1.3 on 2024-11-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_parent_father_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='mother_contact',
            field=models.CharField(max_length=15),
        ),
    ]