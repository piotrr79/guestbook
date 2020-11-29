from django.conf.urls import include, url
from django.http import HttpResponse
from guestbook import views
from guestbook.views import GuestbookCreate

def index(request):
    return HttpResponse("Hello, world. You're at the guestbook index.")

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<guestbook_id>\d+)/$', views.detail, name='detail'),
    url(r'addentry/add/$', GuestbookCreate.as_view(), name='addentry'),
]