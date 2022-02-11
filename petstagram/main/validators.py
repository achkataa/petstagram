from django.core.exceptions import ValidationError


def only_letters_validator(value):
    for x in value:
        if not x.isalpha():
            raise ValidationError('value should contain only latters')


def validate_file_max_size_in_mb(value):
    filesize = value.file.size
    megabyte_limit = 5
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))