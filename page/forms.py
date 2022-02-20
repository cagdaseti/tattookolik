from django import forms
from .models import Carousel,Page
from crispy_forms.helper import FormHelper

class CarouselModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
    class Meta:
        model = Carousel
        # fields = '__all__' # Dont Use This - all fields include
        # exclude = ['title'] # Dont Use This - all fields include without 'title'
        fields = [
            'title',
            'cover_image',
            'status',
        ]


class PageModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
    class Meta:
        model = Page
        fields = [
            'title',
            'cover_image',
            'content',
            'status',
        ]