# Generated by Django 2.1.7 on 2019-03-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals_app', '0004_auto_20190309_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minerals',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
