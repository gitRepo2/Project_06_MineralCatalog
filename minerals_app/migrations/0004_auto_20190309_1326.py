# Generated by Django 2.1.7 on 2019-03-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals_app', '0003_auto_20190307_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minerals',
            name='category',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='cleavage',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='color',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='crystal_habit',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='crystal_symmetry',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='crystal_system',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='diaphaneity',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='formula',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='group',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='image_caption',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='image_filename',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='luster',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='mohs_scale_hardness',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='optical_properties',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='refractive_index',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='specific_gravity',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='streak',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='strunz_classification',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='minerals',
            name='unit_cell',
            field=models.CharField(default=None, max_length=255),
        ),
    ]