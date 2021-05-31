from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Task, Notification

UserModel = get_user_model()


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
        ('Android', 'Android'),
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

    def save(self, commit=True):
        # Call save of the super of your own class,
        # which is UserCreationForm.save() which calls user.set_password()
        user = super(CustomUserCreationForm, self).save(commit=False)

        # Add the things your super doesn't do for you
        user.department = self.cleaned_data['department']
        user.status = self.cleaned_data['status']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class LoginUserForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        self.fields['username'].widget.attrs.update({'name': 'username', 'placeholder': 'Username', 'class': 'input'})
        self.fields['password'].widget.attrs.update({'name': 'password1', 'placeholder': 'Password', 'class': 'input'})
        self.fields['password'].label = ''
        self.fields['username'].label = ''
        # self.error_messages['invalid_login'] = ''
        # self.error_messages['inactive'] = ''


class CreateTaskForm(forms.ModelForm):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'name': 'title', 'placeholder': 'Title', 'class': 'input'}))
    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={'name': 'description', 'placeholder': 'Description', 'class': 'input'}))

    executor = forms.ModelChoiceField(label="", queryset=CustomUser.objects.all().order_by('first_name'),
                                      empty_label="Employee", widget=forms.Select(
            attrs={'name': 'executor', 'style': 'width:355px;cursor: pointer;', 'class': 'input'}))

    class Meta:
        model = Task
        fields = ('title', 'description', 'executor')

    def __init__(self, *args, **kwargs):
        self.task_setter = kwargs.pop('task_setter')
        super(CreateTaskForm, self).__init__(*args, **kwargs)


class TaskTrackForm(forms.ModelForm):
    completed = forms.BooleanField(label="", widget=forms.CheckboxInput(
        attrs={'name': 'a', 'class': 'checkbox', 'type': 'checkbox'}))

    class Meta:
        model = Task
        fields = ('completed',)


class CreateNotificationForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.TextInput(
        attrs={'name': 'notification_text', 'placeholder': 'Description', 'class': 'input'}))

    class Meta:
        model = Notification
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(CreateNotificationForm, self).__init__(*args, **kwargs)
