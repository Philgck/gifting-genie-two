from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Planner(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField()
    event_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name
# Create your models here.
