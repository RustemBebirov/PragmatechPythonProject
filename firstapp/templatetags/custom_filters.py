from django.template import Library

register = Library()

@register.filter
def boyuk_herf(title):
    return title.upper()


@register.filter
def kicik_herf(title):
    return title.lower()

@register.filter
def cap(title):
    return title.capitalize()