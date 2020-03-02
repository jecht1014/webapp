from django.db import models
from django.utils import timezone
from django.core import validators

class Company(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Kind(models.Model):
    kind = models.CharField(max_length=100)
    def __str__(self):
        return self.kind

class Food(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    taste = models.CharField(max_length=100, blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    value = models.IntegerField(default=0, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
    remarks = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name