# Generated by Django 4.2.11 on 2024-05-08 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_api', '0003_commodity_fk_cmd_group_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='fk_cmd_group_id',
        ),
    ]
