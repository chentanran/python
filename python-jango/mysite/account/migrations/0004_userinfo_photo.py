# Generated by Django 3.0.2 on 2020-01-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
