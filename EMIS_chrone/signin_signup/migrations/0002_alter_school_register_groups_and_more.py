# Generated by Django 4.2.4 on 2023-08-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('signin_signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_register',
            name='groups',
            field=models.ManyToManyField(related_name='school_users', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='school_register',
            name='user_permissions',
            field=models.ManyToManyField(related_name='school_users', to='auth.permission'),
        ),
    ]
