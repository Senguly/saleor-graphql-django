from django.db import models

from ..account.models import User
from . import JobStatus


class Job(models.Model):
    status = models.CharField(
        max_length=50, choices=JobStatus.choices(), default=JobStatus.PENDING
    )
    user = models.ForeignKey(User, related_name="jobs", on_delete=models.CASCADE)
    content_file = models.FileField(upload_to="csv_files", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True)
