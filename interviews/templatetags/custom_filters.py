from django import template

register = template.Library()

@register.filter
def exclude_first(queryset):
    return queryset[1:]
