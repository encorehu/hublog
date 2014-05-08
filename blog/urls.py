# -*- coding: utf-8 -*-

# python.
#import datetime
# ------------------------------------------------------------

# django.
from django.conf.urls import *
from django.core.paginator import Paginator, InvalidPage
from django.views.generic import DetailView, ListView

# ------------------------------------------------------------

#from forms  import AForm,BForm
# ------------------------------------------------------------

urlpatterns = patterns('',

    url(r'^$',     'hublog.views.index',name='hublog_index'),

)
