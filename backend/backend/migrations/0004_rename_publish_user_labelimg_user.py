# Generated by Django 3.2.8 on 2021-12-22 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20211222_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labelimg',
            old_name='publish_user',
            new_name='user',
        ),
    ]