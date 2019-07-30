# get_user_model returns the current default user model which is use in this project
from django.contrib.auth import get_user_model
# UserCreationForm is builtin form to create new user with existing model
from django.contrib.auth.forms import UserCreationForm 


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"