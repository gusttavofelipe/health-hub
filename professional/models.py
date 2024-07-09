from django.db import models
from utils.base_model import BaseModel, get_upload_path


class Professional(BaseModel):
    full_name = models.CharField("Full Name", max_length=255, blank=False, null=False)
    picture = models.ImageField(
        "Picture", upload_to=get_upload_path, blank=True, null=True
    )
    birth_date = models.DateTimeField("Birth Date", auto_now=False, auto_now_add=False)
    phone_number = models.CharField(
        "Phone Number", max_length=255, blank=True, null=True
    )
    email = models.EmailField(
        "E-mail", max_length=254, unique=True, blank=True, null=True
    )

    class Meta:
        verbose_name = "Professional"
        verbose_name_plural = "Professionals"
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name
