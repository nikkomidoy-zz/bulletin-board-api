from django.db import models
from model_utils.models import TimeStampedModel


class Board(TimeStampedModel):
    name = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def get_number_of_threads(self):
        return self.threads.count()
