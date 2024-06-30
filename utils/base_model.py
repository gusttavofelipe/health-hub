import inspect
import os
import uuid
from django.db import models
from pathlib import Path


class BaseModel(models.Model):
    uuid = models.UUIDField("UUID", default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True


def get_upload_path(instance, filename):
    model_class = instance.__class__
    module_file = Path(inspect.getfile(model_class)).resolve()
    parent_dir_name = module_file.parent.name
    folder_name = instance.full_name.replace(" ", "_").lower()

    return os.path.join(parent_dir_name, folder_name, filename)
