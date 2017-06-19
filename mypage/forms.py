from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class FindUserNameForm(forms.Form):
    email = EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))


    def __init__(self, *args, **kwargs):
        super(FindUserNameForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['email'].widget.attrs['placeholder'] = "email : example@abc.com"
        self.fields['email'].widget.attrs['class'] = "form-control"

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            pass
        else:
            raise forms.ValidationError("There are no accounts signed up with the email you entered. It is recommended to join a new one.")
        return data

class FindPasswordForm(forms.Form):
    email = forms.EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))
    username = forms.CharField(label=_("username"),max_length=50)


    def __init__(self, *args, **kwargs):
        super(FindPasswordForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['email'].widget.attrs['placeholder'] = "email : example@abc.com"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['username'].widget.attrs['placeholder'] = "username"
        self.fields['username'].widget.attrs['class'] = "form-control"

    def clean(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if User.objects.filter(email=email, username=username).exists():
            pass
        else:
            raise forms.ValidationError("There is no information about the ID and email you entered. We encourage you to join.")
        return User.objects.filter(email=email, username=username)


class FindPasswordForm(forms.Form):
    email = forms.EmailField(label=_("Email address"), required=True,
        help_text=_("Required."))
    username = forms.CharField(label=_("username"),max_length=50)


    def __init__(self, *args, **kwargs):
        super(FindPasswordForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['email'].widget.attrs['placeholder'] = "email : example@abc.com"
        self.fields['email'].widget.attrs['class'] = "form-control"
        self.fields['username'].widget.attrs['placeholder'] = "username"
        self.fields['username'].widget.attrs['class'] = "form-control"

    def clean(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if User.objects.filter(email=email, username=username).exists():
            pass
        else:
            raise forms.ValidationError("There is no information about the ID and email you entered. We encourage you to join.")
        return User.objects.filter(email=email, username=username)

class ChangePwForm(forms.Form):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
        )
    new_password2 = forms.CharField(
        label=(u'Verify Password'), 
        widget = forms.PasswordInput(render_value=False)
        )


    def __init__(self, *args, **kwargs):
        super(ChangePwForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['new_password1'].widget.attrs['placeholder'] = "password"
        self.fields['new_password1'].widget.attrs['class'] = "form-control"
        self.fields['new_password2'].widget.attrs['placeholder'] = "password check"
        self.fields['new_password2'].widget.attrs['class'] = "form-control"

    def clean(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']
        if password1==password2:
            pass
        else:
            raise forms.ValidationError("The two passwords you entered do not match. Please re-enter")
            return password1

class DeleteUserForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
        )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DeleteUserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        self.fields['password'].widget.attrs['placeholder'] = "password"
        self.fields['password'].widget.attrs['class'] = "form-control"

    def clean(self):
        password = self.cleaned_data['password']
        user = User.objects.get(username=self.user)
        if user.check_password(password):
            pass
        else:
            raise forms.ValidationError("The current password and the password you entered do not match. Please enter again")
            return password
