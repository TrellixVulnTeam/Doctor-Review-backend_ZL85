# Generated by Django 3.2.8 on 2022-06-06 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20220606_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('password', models.CharField(default='123456', max_length=64)),
            ],
        ),
        migrations.AddConstraint(
            model_name='userinfo',
            constraint=models.UniqueConstraint(fields=('user_name', 'email'), name='unique_user'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='given_approval', to='backend.userinfo'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='given_comment', to='backend.userinfo'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
