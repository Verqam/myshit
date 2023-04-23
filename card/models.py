from django.db import models


class FlashCard(models.Model):
    question = models.TextField()
    answer = models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question