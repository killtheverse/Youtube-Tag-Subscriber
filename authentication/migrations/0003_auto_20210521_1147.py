# Generated by Django 3.0.5 on 2021-05-21 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210520_0804'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlacklistedAccessToken',
        ),
        migrations.DeleteModel(
            name='BlackListedRefreshToken',
        ),
    ]