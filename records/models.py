from django.db import models
from professional.models import Professional
from utils.base_model import BaseModel, get_upload_path


class PersonalHealthRecord(BaseModel):
    full_name = models.CharField("Full Name", max_length=255, blank=False, null=False)
    picture = models.ImageField(
        "Picture", upload_to=get_upload_path, blank=True, null=True
    )
    age = models.IntegerField("Age", blank=False, null=False)
    locality = models.CharField("Locality", max_length=100, blank=False, null=False)
    street = models.CharField("Street", max_length=100, blank=False, null=False)
    reference = models.CharField("Reference", max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        "Phone Number", max_length=255, blank=True, null=True
    )
    email = models.EmailField(
        "E-mail", max_length=254, unique=True, blank=True, null=True
    )
    household_size = models.IntegerField("Household Size", null=True, blank=True)
    health_issue = models.CharField(
        "Health Issue", max_length=255, null=True, blank=True
    )
    symptoms = models.TextField("Symptoms", max_length=530, blank=True, null=True)
    last_recorded_by = models.ForeignKey(Professional, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Personal Health Record"
        verbose_name_plural = "Personal Health Records"
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name
