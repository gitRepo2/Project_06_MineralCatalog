# Generated by Django 2.1.7 on 2019-03-06 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='minerals',
            name='diaphaneity',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
