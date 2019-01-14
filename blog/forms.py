from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Post, Pogar, Sevsk, Calendar


class PogarForm(forms.ModelForm):
    class meta:
        model = Pogar
        fields = ('title', 'text')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class SevskForm(forms.ModelForm):
    class Meta:
        model = Sevsk
        fields = ('title', 'text')

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ('title', 'text')
