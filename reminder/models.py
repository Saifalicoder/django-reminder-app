from django.db import models

class Reminder(models.Model):

    REMINDER_METHOD_CHOICES = (
        ('SMS', 'SMS'),
        ('Email', 'Email'),
    )
    reminder_method = models.CharField(max_length=10, choices=REMINDER_METHOD_CHOICES ,null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.message