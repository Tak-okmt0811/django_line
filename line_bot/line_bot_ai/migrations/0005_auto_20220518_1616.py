# Generated by Django 3.2.8 on 2022-05-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot_ai', '0004_auto_20220518_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
