import factory
from factory.django import DjangoModelFactory

from boards.factories import BoardFactory
from threads.models import Thread


class ThreadFactory(DjangoModelFactory):
    board = factory.SubFactory(BoardFactory)

    class Meta:
        model = Thread
