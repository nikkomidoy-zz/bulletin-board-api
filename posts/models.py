from django.db import models
from model_utils.models import TimeStampedModel

from bulletin_board.users.models import UserProfile
from threads.models import Thread


class Post(TimeStampedModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    publisher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return f'Post - {self.id}'
