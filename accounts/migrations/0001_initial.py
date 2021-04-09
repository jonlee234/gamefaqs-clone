# Generated by Django 3.0.8 on 2021-04-08 23:23

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('bio', models.CharField(max_length=500)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('platform_choice_field', models.CharField(choices=[('1', 'PC'), ('2', 'PS5'), ('3', 'XSX'), ('4', 'Switch'), ('5', 'iOS'), ('6', 'Android'), ('7', 'Arcade'), ('8', 'PS4'), ('9', 'PS3'), ('10', 'Xbox One'), ('11', 'Xbox 360'), ('12', 'Sega'), ('13', 'Wii U'), ('14', 'Wii'), ('15', 'PSP'), ('16', 'Vita'), ('17', '3DS'), ('18', 'RetoPy'), ('19', 'Other Systems')], max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
