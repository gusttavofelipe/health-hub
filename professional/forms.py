from django import forms
from django.contrib.auth.models import User
from professional.models import Professional
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    email = forms.EmailField(label="Email", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


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
            # Se o usuário já existir, você pode atualizar os dados aqui se necessário
            # Exemplo: user.email = email
        except User.DoesNotExist:
            user = User(username=email.split("@")[0], email=email)
            user.set_password(password)
            user.save()

        professional = super().save(commit=False)
        professional.user = user
        if commit:
            professional.save()
        return professional
