from django import forms
from django.contrib.auth.models import User
from professional.models import Professional
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(username=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid email or password")
        return self.cleaned_data

    def get_user(self):
        return self.user


class ProfessionalForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm password", widget=forms.PasswordInput
    )

    class Meta:
        model = Professional
        fields = [
            "full_name",
            "phone_number",
            "email",
            "birth_date",
            "password",
            "confirm_password",
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        try:
            user = User.objects.get(username=email.split("@")[0])
        except User.DoesNotExist:
            user = User(username=email.split("@")[0], email=email)
            user.set_password(password)
            user.save()

        professional = super().save(commit=False)
        professional.user = user
        if commit:
            professional.save()
        return professional
