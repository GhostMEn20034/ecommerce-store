from django.utils.crypto import get_random_string


def generate_random_number(length):
    return get_random_string(length, allowed_chars='0123456789')
