from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Part Time','Part time'),
    ('Full Time','Full Time'),
)
class Job(models.Model):
    titel = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=400)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.titel