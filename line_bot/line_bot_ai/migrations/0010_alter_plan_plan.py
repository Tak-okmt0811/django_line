# Generated by Django 3.2.8 on 2022-05-18 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('line_bot_ai', '0009_id_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='line_bot_ai.menu'),
        ),
    ]
