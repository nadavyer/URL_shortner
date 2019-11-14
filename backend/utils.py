from random import choice
import string
import validators

def gen_code_for_long_url(long_url): 
    chars = string.ascii_letters + string.digits
    length = 5
    code = ''.join(choice(chars) for x in range(length))

    return code


def prepare_for_url_validation(long_url):
    long_url_7_prefix = long_url[:7]
    long_url_8_prefix = long_url[:8]
    if long_url_7_prefix == 'http://' or long_url_8_prefix == 'https://':
        return long_url
    return 'http://' + long_url


def validate_url(long_url):
    url = prepare_for_url_validation(long_url)
    return validators.url(url) and url


def long_url_from_request(request):
    request_json = request.json
    long_url = request_json['longUrl']
    return long_url