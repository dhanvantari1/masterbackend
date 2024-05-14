# Generated by Django 4.2.11 on 2024-05-08 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_api', '0002_tenantmaster_rename_cmd_code_commodity_tenant_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='fk_cmd_group_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='master_api.commoditygroup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commodity',
            name='tenant_code',
            field=models.CharField(max_length=10),
        ),
    ]
