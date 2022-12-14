from django import forms

from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'Name',
            'DOB','DOJ','Department',
            'Post','Address','City','Country',
            'ZipCode','State','Active','Leave_count','on_leave'
        ]

        widget = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'DOB': forms.DateInput(attrs={'class':'form-control'}),
            'DOJ': forms.DateInput(attrs={'class':'form-control'}),
            'Department': forms.TextInput(attrs={'class':'form-control'}),
            'Post': forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
            'City': forms.TextInput(attrs={'class':'form-control'}),
            'Country': forms.TextInput(attrs={'class':'form-control'}),
            'ZipCode': forms.NumberInput(attrs={'class':'form-control'}),
            'State': forms.TextInput(attrs={'class':'form-control'}),
            'Active': forms.RadioSelect(attrs={'class':'form-control'}),
            'Leave_count': forms.NumberInput(attrs={'class':'form-control'}),
            'on_leave': forms.RadioSelect(attrs={'class':'form-control'}),
            
        }