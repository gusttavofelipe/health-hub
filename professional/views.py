from django.urls import reverse_lazy
from professional.forms import ProfessionalForm
from professional.models import Professional
from django.contrib import messages
from django.views.generic import CreateView


class ProfessionalCreateView(CreateView):
    model = Professional
    form_class = ProfessionalForm
    template_name = "professional/register.html"
    success_url = reverse_lazy("records:home")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Registered successfully!")
        return super().form_valid(form)
