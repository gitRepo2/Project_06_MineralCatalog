from django.db import models


class Minerals(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255, null=True, blank=True, default=None)
    image_caption = models.CharField(max_length=255, null=True, blank=True, default=None)
    category = models.CharField(max_length=255, null=True, blank=True, default=None)
    formula = models.CharField(max_length=255, null=True, blank=True, default=None)
    strunz_classification = models.CharField(max_length=255, null=True, blank=True, default=None)
    crystal_system = models.CharField(max_length=255, null=True, blank=True, default=None)
    unit_cell = models.CharField(max_length=255, null=True, blank=True, default=None)
    color = models.CharField(max_length=255, null=True, blank=True, default=None)
    crystal_symmetry = models.CharField(max_length=255, null=True, blank=True, default=None)
    cleavage = models.CharField(max_length=255, null=True, blank=True, default=None)
    mohs_scale_hardness = models.CharField(max_length=255, null=True, blank=True, default=None)
    luster = models.CharField(max_length=255, null=True, blank=True, default=None)
    streak = models.CharField(max_length=255, null=True, blank=True, default=None)
    diaphaneity = models.CharField(max_length=255, null=True, blank=True, default=None)
    optical_properties = models.CharField(max_length=255, null=True, blank=True, default=None)
    group = models.CharField(max_length=255, null=True, blank=True, default=None)
    refractive_index = models.CharField(max_length=255, null=True, blank=True, default=None)
    crystal_habit = models.CharField(max_length=255, null=True, blank=True, default=None)
    specific_gravity = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return self.name
