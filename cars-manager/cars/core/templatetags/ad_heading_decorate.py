from django import template

register = template.Library()


@register.filter(name='cut_heading')
def decorate_ad_heading(value):
    chars = [x for x in value]
    if len(chars) > 17:
        return value[0:18] + '...'
    else:
        return value
