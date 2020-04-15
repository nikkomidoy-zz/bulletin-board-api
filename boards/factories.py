import factory
from factory.django import DjangoModelFactory

from boards.models import Board


class BoardFactory(DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('sentence')

    class Meta:
        model = Board
        django_get_or_create = ('name',)
