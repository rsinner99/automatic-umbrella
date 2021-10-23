from django.utils.http import urlencode
from django.urls import reverse as original_reverse

def reverse(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = original_reverse(*args, **kwargs)

    if get:
        url += '?' + urlencode(get)

    return url