# Generated by Django 3.2 on 2023-04-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_useraccount_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutstandingToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Outstanding Token',
                'verbose_name_plural': 'Outstanding Tokens',
            },
        ),
        migrations.CreateModel(
            name='TokenBlacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=500, unique=True)),
                ('blacklisted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Token Blacklist',
                'verbose_name_plural': 'Token Blacklist',
            },
        ),
    ]