# Generated by Django 2.2.1 on 2019-05-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_name', models.CharField(max_length=255)),
                ('es_icon', models.ImageField(null=True, upload_to='')),
                ('es_rating', models.IntegerField(default=0, null=True)),
                ('es_site', models.CharField(max_length=100)),
                ('es_phone', models.CharField(max_length=11)),
                ('es_cnpj', models.CharField(max_length=14)),
                ('es_street', models.CharField(max_length=100)),
                ('es_district', models.CharField(max_length=50)),
                ('es_state', models.CharField(max_length=2)),
                ('es_city', models.CharField(max_length=100)),
                ('es_number', models.IntegerField()),
                ('es_zip_code', models.CharField(max_length=8)),
            ],
        ),
    ]