from django.db.models import Count
from django import template
import markdown2
from minerals_app.models import Minerals

register = template.Library()


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to html"""
    html_body = markdown2.markdown(markdown_text)
    return html_body
