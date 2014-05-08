# -*- coding: utf-8 -*-

# python.
#
# ------------------------------------------------------------

# django.
from django.db import models
from django.db.models import Q
# ------------------------------------------------------------

# 3dpart.
#
# ------------------------------------------------------------

# blog.
# ------------------------------------------------------------

# config.
# ------------------------------------------------------------

class BlogManager(models.Manager):
    def for_user(self, user):
        user_blogs = Q(user__exact=user)
        return self.filter(user_blogs)
