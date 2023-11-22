from django import template
from shop import models
from extensions.Show import show_now

register=template.Library()

@register.simple_tag

def website_name(name='دیجی‌کالا'):
    return name

@register.simple_tag
def testing():
    return show_now.show_it



