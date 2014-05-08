# -*- coding: utf-8 -*-

# python.
#import datetime
#import urllib
# ------------------------------------------------------------

# django.
from django.contrib.sitemaps import Sitemap
from .models import Blog
# ------------------------------------------------------------

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
