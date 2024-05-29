from django.db import models
from django.utils import timezone

class SurveyResult(models.Model):
    total_value = models.IntegerField()
    recorded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Result: {self.total_value} at {self.recorded_at}'

class VoiceFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name