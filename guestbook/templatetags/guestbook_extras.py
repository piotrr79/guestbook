from django.template import RequestContext, loader
from django.http import HttpResponse
from django import template
register = template.Library()

          
@register.inclusion_tag('guestbook/guestbook_form.html')
def addentryform():
    return 
