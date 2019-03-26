from django.core.management.base import BaseCommand
from minerals_app.models import Minerals

import json

file_name = "minerals.json"

"""Command to prepopulate the db: python manage.py load_mineral_data
   More info: https://docs.djangoproject.com/en/2.1/howto/
   custom-management-commands/"""

class Command(BaseCommand):
    """Loads the data from the .json file and fills it into the database"""
    def handle(self, *args, **options):
        with open(file_name, encoding='utf-8') as file:
            minerals = json.load(file)

        for mineral in minerals:
            Minerals(
                name=mineral.get('name', ''),  # adds '' if key is not found
                image_filename=mineral.get('image filename', ''),
                image_caption=mineral.get('image caption', ''),
                category=mineral.get('category', ''),
                formula=mineral.get('formula', ''),
                strunz_classification=mineral.get('strunz classification', ''),
                crystal_system=mineral.get('crystal system', ''),
                unit_cell=mineral.get('unit cell', ''),
                color=mineral.get('color', ''),
                crystal_symmetry=mineral.get('crystal symmetry', ''),
                cleavage=mineral.get('cleavage', ''),
                mohs_scale_hardness=mineral.get('mohs scale hardness', ''),
                luster=mineral.get('luster', ''),
                streak=mineral.get('streak', ''),
                diaphaneity=mineral.get('diaphaneity', ''),
                optical_properties=mineral.get('optical properties', ''),
                group=mineral.get('group', ''),
                refractive_index=mineral.get('refractive index', ''),
                crystal_habit=mineral.get('crystal habit', ''),
                specific_gravity=mineral.get('specific gravity', '')
            ).save()
            self.stdout.write(self.style.SUCCESS(
                'Yey. Mineral has been successfully added to the Minerals db'
            ))

