from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by a delimiter"""
    return value.split(arg)

@register.filter
def trim(value):
    """Trim whitespace from a string"""
    return value.strip()

@register.filter 
def add(value, arg):
    """Add two values"""
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return value
