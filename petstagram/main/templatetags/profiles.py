from django import template

from petstagram.accounts.models import PetstagramUser

register = template.Library()

@register.simple_tag()
def has_profile():
    return PetstagramUser.objects.count() > 0