from django.db import models


class Journal_entry(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
