import factory
from factory.django import DjangoModelFactory

from posts.models import Post
from threads.factories import ThreadFactory


class PostFactory(DjangoModelFactory):
    thread = factory.SubFactory(ThreadFactory)
    description = factory.Sequence(lambda n: "This what it looks like for Post %03d" % n)

    class Meta:
        model = Post
