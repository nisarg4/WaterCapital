# Generated by Django 2.1 on 2018-09-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_date', models.DateField()),
                ('value', models.FloatField()),
                ('type', models.TextField(max_length=254)),
                ('name', models.TextField(max_length=254)),
            ],
        ),
    ]
