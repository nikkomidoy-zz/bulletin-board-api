from django.db import models
from model_utils.models import TimeStampedModel

from boards.models import Board
from utils.models import format_date_object_to_str


class Thread(TimeStampedModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='threads')
    is_draft = models.BooleanField(default=False)
    is_sticky = models.BooleanField(default=False)

    def __str__(self):
        return f'Thread - {self.id}'

    @property
    def date_of_last_reply(self):
        """
        Return the date last reply from the posts

        Hint: Order querysets by date, use annotate or aggregate if needed.
        """
        return format_date_object_to_str(
            self.posts.latest('created').created.date()
        )

    @property
    def who_posted_last(self):
        """
        Return the last publisher who posted

        Hint: Order querysets from date get the first publisher
        """
        return (self.posts.latest('created').publisher.user.get_full_name()
                or 'No name')
