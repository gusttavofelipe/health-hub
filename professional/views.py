from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from professional.forms import LoginForm, ProfessionalForm
from professional.models import Professional
from django.contrib import messages
from django.views.generic import CreateView


class ProfessionalCreateView(CreateView):
    model = Professional
    form_class = ProfessionalForm
    template_name = "professional/register.html"
    success_url = reverse_lazy("records:home")

    def form_valid(self, form):
        professional = form.save(commit=False)
        professional.save()

        user = authenticate(
            username=professional.user.username, password=form.cleaned_data["password"]
        )

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Registered and logged in successfully!")
        else:
            messages.warning(
                self.request, "Unable to log in automatically. Please log in manually."
            )
            return redirect("professionals:login")

        return super().form_valid(form)


class ProfessionalLoginView(View):
    form_class = LoginForm
    template_name = "professional/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect("records:home")
            else:
                messages.error(request, "Invalid email or password")

        return render(request, self.template_name, {"form": form})


class ProfessionalLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect("records:home")
