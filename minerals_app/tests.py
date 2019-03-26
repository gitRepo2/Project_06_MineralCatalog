from django.urls import reverse
from django.test import TestCase

from .models import Minerals


class MineralsModelTests(TestCase):
    """Used command to dump data:
    python manage.py dumpdata > test_minerals_fixture.json
    https://coderwall.com/p/kogbla/django-fixture-dumpdata-loaddata-and-integrity-error
    python manage.py dumpdata --exclude=contenttypes --exclude=auth.Permission > initial_data.json
    database will be filled before calling the setup method."""
    fixtures = ['test_minerals_fixture.json']

    def setUp(self):
        self.mineral = Minerals.objects.create(
            name="Amineral",
            color="black",
            crystal_symmetry="anySymmetry22"
        )

    def test_step_creation(self):
        self.assertIn(self.mineral, Minerals.objects.all())

    def test_mineral_string(self):
        """String version of Mineral should contain the name and e.g. color"""
        self.assertIn(self.mineral.name, str(self.mineral))
        self.assertIn(self.mineral.color, str(self.mineral.color))


class ViewTests(TestCase):
    def setUp(self):
        self.mineral = Minerals.objects.create(
            name="Cmineral",
            color="red",
            crystal_symmetry="anySymmetry66"
        )
        self.mineral2 = Minerals.objects.create(
            name="Bmineral",
            color="pink",
            crystal_symmetry="anySymmetry44"
        )

    def test_mineral_list_view(self):
        """The mineral_list view should:
           * return a 200
           * have self.mineral in the context
           * use the minerals_app/mineral_list.html template
        """
        resp = self.client.get(reverse('minerals_app:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals_app/mineral_list.html')

    def test_mineral_detail_view(self):
        """The mineral_detail view should:
           * return a 200
           * have self.mineral in the context
           * use the minerals_app/mineral_detail.html template
        """
        resp = self.client.get(reverse('minerals_app:detail',
                                       kwargs={'pk': self.mineral2.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['mineral'], self.mineral2)
        self.assertTemplateUsed(resp, 'minerals_app/mineral_detail.html')
