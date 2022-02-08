from tkinter import Widget
from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelsForm):
    name=forms.CharField(max_length=128, help_text="Please enter the categiry name.")
    views = forms.IntegersField(Widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegersField(Widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), requited =False)

#class to provide additional info on the form
class Meta:
    #provide associaltion btwn ModelForm and model
    model=Category
    fields = ('name',)

class PageForm (forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URl of the page.")
    views= forms.IntegerField(widget=forms.HiddenInput(), initial=0)

class Meta:
    model = Page
    exclude=('category')   