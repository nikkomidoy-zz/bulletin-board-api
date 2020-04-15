import factory
from factory.django import DjangoModelFactory

from bulletin_board.users.models import UserProfile


class UserFactory(DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False


class UserProfileFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    about = factory.Sequence(lambda n: "About %03d" % n)
    birth_date = factory.Faker('date_object')

    class Meta:
        model = UserProfile
