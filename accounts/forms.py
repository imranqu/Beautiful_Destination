from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    model=get_user
    class Meta:
        fields=[
            'username','password1','password2','email'
        ]