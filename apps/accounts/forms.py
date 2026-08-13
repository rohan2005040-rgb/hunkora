from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


# ==========================================
# 1. Registration Form
# ==========================================
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Enter your email",
                "class": "form-control",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Choose a username",
                "class": "form-control",
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Create password",
                "class": "form-control",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email")


# ==========================================
# 2. Login Form
# ==========================================
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username",
                "class": "form-control",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter password",
                "class": "form-control",
            }
        )
    )


# ==========================================
# 3. User Basic Info Update Form
# ==========================================
class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        )
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


# ==========================================
# 4. User Profile (Avatar & Address) Update Form
# ==========================================
class ProfileUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={"class": "form-control", "accept": "image/*"}
        ),
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "017XXXXXXXX"}
        ),
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Full Shipping Address",
            }
        ),
    )

    class Meta:
        model = UserProfile
        fields = ["avatar", "phone_number", "address"]