from django import template

from apps.main.models import Partners, MeContact


register = template.Library()


@register.simple_tag()
def me_contact():
    return MeContact.objects.get()


@register.simple_tag()
def partners():
    return Partners.objects.get()
