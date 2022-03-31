from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/info_cat.html')
def info_cat():
    title = 'Изученные технологие'
    title_seconds = 'Изучаемые технологии'
    return {'title': title, 'title2': title_seconds}
