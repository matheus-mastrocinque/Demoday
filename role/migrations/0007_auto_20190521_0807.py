# Generated by Django 2.2.1 on 2019-05-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0006_auto_20190521_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinterests',
            name='tipos_role',
            field=models.CharField(max_length=50),
        ),
    ]