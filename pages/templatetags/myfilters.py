from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='addid')
def addid(value, arg):
    return value.as_widget(attrs={'id': arg})

@register.filter(name='tostring')
def tostring(value):
    return str(value)