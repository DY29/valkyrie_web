# Generated by Django 2.1.4 on 2019-01-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181231_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_lc',
            name='u',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contract_lc',
            name='v',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contract_lc',
            name='w',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
