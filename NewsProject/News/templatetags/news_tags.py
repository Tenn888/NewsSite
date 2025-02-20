from News.models import Category
from django import template
from django.db.models import Count, F

register = template.Library()

@register.inclusion_tag('News/list_categories.html')
def show_categories(arg1='Categories', arg2='list'):
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    if not categories:
        categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {
        'categories': categories,
        'arg1': arg1,
        'arg2': arg2
    }