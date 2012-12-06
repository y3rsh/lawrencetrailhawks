from django.template import Library

from ..models import News


register = Library()


@register.assignment_tag(takes_context=True)
def get_latest_news(context, num):
    return News.published_objects.all()[:num]
