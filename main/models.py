from django.db import models
from django.utils import timezone

class SurveyResult(models.Model):
    total_value = models.IntegerField()
    recorded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Result: {self.total_value} at {self.recorded_at}'
