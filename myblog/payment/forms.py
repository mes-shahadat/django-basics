from django import forms
from payment.models import ModelStudent, ModelTeacher, ModelContractor, ModelCenter, ModelCenterStudent,ProxyModelCenterStudent


class FormModelStudent(forms.ModelForm):
    class Meta:
        model = ModelStudent
        fields = ('name','age','fees')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'fees':forms.TextInput(attrs={'class':'form-control'})
        }


class FormModelTeacher(forms.ModelForm):
    class Meta:
        model = ModelTeacher
        fields = ('name','age','date','salary')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.TextInput(attrs={'class':'form-control'})
        }
        

class FormModelContractor(forms.ModelForm):
    class Meta:
        model = ModelContractor
        fields = ('name','age','date','payment')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.TextInput(attrs={'class':'form-control'}),
            'payment':forms.TextInput(attrs={'class':'form-control'})
        }

class FormModelCenter(forms.ModelForm):
    class Meta:
        model = ModelCenter
        fields = ('center_name','city')
        widgets = {
            'center_name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
        }

class FormModelCenterStudent(forms.ModelForm):
    class Meta:
        model = ModelCenterStudent
        fields = ('center_name','city','name','roll')
        widgets = {
            'center_name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.TextInput(attrs={'class':'form-control'})
        }

class FormProxyModelCenterStudent(forms.ModelForm):
    class Meta:
        model = ProxyModelCenterStudent
        fields = ('center_name','city','name','roll')
        widgets = {
            'center_name':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.TextInput(attrs={'class':'form-control'})
        }
