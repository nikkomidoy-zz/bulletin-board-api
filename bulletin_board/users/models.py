import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    following = models.ManyToManyField('self', null=True, blank=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    about = models.TextField(null=True, blank=True)
    birth_date = models.DateField()
    hometown = models.CharField(max_length=32, null=True, blank=True)
    present_location = models.CharField(max_length=32, null=True, blank=True)
    geo_location = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        full_name = self.user.get_full_name() or 'No full name'
        return f'Profile - {full_name}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
