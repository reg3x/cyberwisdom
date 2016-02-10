from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    userId = models.CharField(max_length=12)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=40, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=100, blank=True)