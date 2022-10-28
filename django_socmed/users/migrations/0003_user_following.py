# Generated by Django 3.2.15 on 2022-10-15 15:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221015_1552'),
        ('users', '0002_auto_20220912_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='accounts.Contact', to=settings.AUTH_USER_MODEL),
        ),
    ]
