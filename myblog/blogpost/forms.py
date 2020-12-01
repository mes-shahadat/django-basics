from django import forms
from blogpost.models import ModelPost
from django.contrib.auth.models import User


class FormContact(forms.Form):
    sender_name = forms.CharField(required=True,widget=forms.TextInput(attrs={ 'class':'form-control'}))
    subject=forms.CharField(required=True,widget=forms.TextInput(attrs={ 'class':'form-control'}))
    message=forms.CharField(required=True,widget=forms.Textarea(attrs={ 'class':'form-control'}))
    contact_email=forms.EmailField(required=True,widget=forms.TextInput(attrs={ 'class':'form-control'}))

class FormModelPost(forms.ModelForm):
    # users = forms.ModelMultipleChoiceField(queryset=User.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={ 'class':'custom-select'}))# can't create cause i don't know ajax and json. in short rest api
    class Meta:
        model = ModelPost
        fields = ('title','desc')
        labels = {'desc':'description'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }