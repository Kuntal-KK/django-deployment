from django import template

register = template.Library()

@register.filter(name='cut_string')
def cut(value,arg):
    """cuts out all the values from 'arg' from the string"""

    return value.replace(arg,'')

# register.filter('cut_string',cut)
