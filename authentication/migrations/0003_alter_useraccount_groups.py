# Generated by Django 3.2 on 2023-04-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0002_auto_20230426_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
    ]
