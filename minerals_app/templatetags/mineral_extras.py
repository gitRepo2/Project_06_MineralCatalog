from django.db.models import Count
from django import template
import markdown2
from minerals_app.models import Minerals

register = template.Library()


@register.filter('replace_underline')
def replace_underline(text):
    """Replaces underline with a space"""
    return text.replace('_', ' ')
