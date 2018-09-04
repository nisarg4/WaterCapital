# Generated by Django 2.1 on 2018-09-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_ssb_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='GS_Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acc_no', models.IntegerField(null=True)),
                ('acc_name', models.TextField(null=True)),
                ('currency', models.TextField(null=True)),
                ('td_quantity', models.FloatField(null=True)),
                ('sd_quantity', models.FloatField(null=True)),
                ('business_date', models.TextField(null=True)),
            ],
        ),
    ]
