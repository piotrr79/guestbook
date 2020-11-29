from django.contrib.admin import AdminSite
from django.contrib import admin

# Register your models here.
from guestbook.models import Guestbook

AdminSite.index_title = 'Guest Book - Admin'
AdminSite.site_header = 'Guest Book - Admin Panel'
AdminSite.site_title = 'Guest Book - Admin Panel'

admin.site.register(Guestbook)
