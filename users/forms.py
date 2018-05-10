from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')