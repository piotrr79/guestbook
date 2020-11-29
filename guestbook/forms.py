from django import forms
from guestbook.models import Guestbook

class GuestbookForm(forms.Form):
    nick = forms.CharField(label='Nick',max_length=255)
    content = forms.CharField(widget=forms.Textarea, label='Message')
