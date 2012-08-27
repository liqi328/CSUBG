from django import template

register = template.Library()


def key(d,key_name):
    return d[key_name]

register.filter('key',key)
