from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.filter(is_safe=True)
def button(value, name_type):
    name_type = name_type.split()
    name, type = name_type[0], name_type[1]
    return mark_safe(f'<button name="{name}" value="{value}" class="btn btn-{type}">{value}</button>')

