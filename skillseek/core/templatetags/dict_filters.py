from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def splitlines(value):
    """
    Splits the string by newline characters and returns a list.
    """
    if not value:
        return []
    return value.splitlines()

@register.filter
def truncate_to_first_period(value):
    """
    Truncates the string up to the first full stop ('.').
    If no full stop is found, returns the whole string.
    """
    if not value:
        return ''
    period_index = value.find('.')
    if period_index == -1:
        return value
    return value[:period_index + 1]
