from django import template

register = template.Library()

@register.filter(name='pieces')
def cut(value, arg):
    if value:
        return [value[x::arg] for x in range(arg)
