from django import forms
from .models import Account


class RegistrationForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'




    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "passwords does not match!"
            )




class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number')


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


