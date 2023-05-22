from django import template

register = template.Library()


@register.filter
def split(text, args):
    term, index = args.split(',')
    return str(text).split(term)[int(index)]
