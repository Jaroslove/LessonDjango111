from django.core.exceptions import ValidationError


def valid_even(value):
    if value % 2 != 0:
        raise ValidationError('%(value)s',
                              params={'value': value}, )


def valid_email(value):
    email = value
    if '.edu' in email:
        raise ValidationError('we dont')


LOCATION = ['Spb', 'Moscow']


def valid_location(value):
    if value in LOCATION:
        raise ValidationError('no')
