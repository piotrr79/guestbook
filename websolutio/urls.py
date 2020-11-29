from django.conf.urls import include, url
from django.contrib import admin
from guestbook import views

urlpatterns=[
    url(r'^', include('guestbook.urls')),
    url(r'^admin/', admin.site.urls),
]
