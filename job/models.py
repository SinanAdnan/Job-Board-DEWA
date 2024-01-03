from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Part Time','Part time'),
    ('Full Time','Full Time'),
)

class Catogery(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Catogeries"


class Job(models.Model):
    titel = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=400)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    job_catogery = models.ForeignKey(Catogery, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titel