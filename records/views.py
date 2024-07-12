from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from records.forms import PersonalHealthRecordForm
from records.models import PersonalHealthRecord
from django.contrib import messages


class HomeView(TemplateView):
    template_name = "records/home.html"


class PersonalHealthCreateView(CreateView):
    model = PersonalHealthRecord
    form_class = PersonalHealthRecordForm
    template_name = "records/register.html"
    success_url = reverse_lazy("records:home")

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Registered successfully!")
        return super().form_valid(form)


class PersonalHealthRecordListView(ListView):
    model = PersonalHealthRecord
    template_name = "records/list.html"
    context_object_name = "records"

    def get_queryset(self):
        user = self.request.user
        queryset = PersonalHealthRecord.objects.filter(last_recorded_by__user=user.id)
        return queryset


class PersonalHealthRecordDetailView(DetailView):
    model = PersonalHealthRecord
    template_name = "records/detail.html"
    context_object_name = "record"
    pk_url_kwarg = "uuid"

    def get_object(self, queryset=None):
        uuid = self.kwargs.get(self.pk_url_kwarg)
        return self.model.objects.get(uuid=uuid)
