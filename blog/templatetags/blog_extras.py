from django import template

register = template.Library()


def penult(alist):
    return alist[-2]


def penult_penult(alist):
    return alist[-3]


def penult_penult_penult(alist):
    return alist[-4]


def get_plus_one(num):
    return num + 1


def get_minus_one(num):
    return num - 1


register.filter('penult', penult)
register.filter('penult_penult', penult_penult)
register.filter('penult_penult_penult', penult_penult_penult)
register.filter('get_plus_one', get_plus_one)
register.filter('get_minus_one', get_minus_one)
