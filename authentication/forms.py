from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="", min_length=2, max_length=20,
                                 widget=forms.TextInput(attrs={'name': 'first_name', 'placeholder': 'First Name',
                                                               'class': 'input'}))
    last_name = forms.CharField(label="", min_length=2, max_length=20,
                                widget=forms.TextInput(
                                    attrs={'name': 'last_name', 'placeholder': 'Last Name', 'class': 'input'}))
    DEPARTMENTS = (
        ('DevOps', 'DevOps'),
        ('ML', 'ML'),
        ('IOS', 'IOS'),
        ('ANDROID', 'ANDROID'),
        ('QA', 'QA')
    )
    department = forms.ChoiceField(label="", choices=DEPARTMENTS, widget=forms.Select(
        attrs={'name': 'department', 'style': 'width:355px;cursor: pointer;', 'class': 'input'}))
    STATUS = (
        ('Employee', 'Employee'),
        ('Employer', 'Employer')
    )
    status = forms.ChoiceField(label="", choices=STATUS,
                               widget=forms.Select(
                                   attrs={'name': 'status', 'style': 'width:355px;cursor: pointer;', 'class': 'input'}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].label = ''
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = ''

        self.fields['password1'].widget.attrs.update({'name': 'password1', 'placeholder': 'Password', 'class': 'input'})
        self.fields['password2'].widget.attrs.update(
            {'name': 'password2', 'placeholder': 'Password Confirmation', 'class': 'input'})

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'name': 'username', 'placeholder': 'Username', 'class': 'input'})
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class LoginUserForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'name': 'username', 'placeholder': 'Username', 'class': 'input'})
        self.fields['password'].widget.attrs.update({'name': 'password1', 'placeholder': 'Password', 'class': 'input'})
        self.fields['password'].label = ''
        self.fields['username'].label = ''

