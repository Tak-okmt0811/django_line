# Generated by Django 3.2.8 on 2022-05-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot_ai', '0008_auto_20220518_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='id',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
    ]