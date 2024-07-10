from django.db import models
from django.contrib.auth.models import User
from utils.base_model import BaseModel, get_upload_path
from django.contrib.auth.hashers import make_password


class Professional(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    password = models.CharField("Password", max_length=128, blank=False, null=False)

    class Meta:
        verbose_name = "Professional"
        verbose_name_plural = "Professionals"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
