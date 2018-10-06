from django import template

register = template.library()


@register.filter(name='cut')
def cut(value, arg):
    """
    this cuts all values of "args" from the string
    :param value:
    :param arg:
    :return:
    """

    return value.replace(arg, '')


# register.filter('cut', cut)
