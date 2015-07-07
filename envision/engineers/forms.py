__author__ = 'trippshealy'
from django import forms
from django.contrib.auth.models import User
from .models import Engineer, Project, Rating


class EngineerForm(forms.ModelForm):
    name = forms.CharField()
    version =forms.CharField()

    class Meta:
        model = Engineer


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating

