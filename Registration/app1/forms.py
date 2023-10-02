from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserData, UserImage

from django.contrib.auth.forms import UserChangeForm


class AdminsignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        # Set a default profile image if no image is provided
        self.fields['profile_image'].widget.attrs['placeholder'] = 'https://img.freepik.com/free-vector/illustration-businessman_53876-5856.jpg?size=626&ext=jpg&ga=GA1.2.722028033.1694535648&semt=ais'
        self.fields['profile_image'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserImage
        fields = ['profile_image']

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if not profile_image:
            raise forms.ValidationError('Please select an image to upload.')
        return profile_image

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CheckUsernameForm(forms.Form):
    username = forms.CharField(max_length=150)


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['height', 'weight', 'image', 'sport_choice']
