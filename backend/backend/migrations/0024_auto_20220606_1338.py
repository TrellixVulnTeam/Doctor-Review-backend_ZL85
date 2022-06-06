# Generated by Django 3.2.8 on 2022-06-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_remove_userinfo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='123456789@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='123456', max_length=64),
        ),
        migrations.AddConstraint(
            model_name='userinfo',
            constraint=models.UniqueConstraint(fields=('user_name', 'email'), name='unique_user'),
        ),
    ]