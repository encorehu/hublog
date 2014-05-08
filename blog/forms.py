# -*- coding: utf-8 -*-

# python.
#
# ------------------------------------------------------------

# django.
from datetime import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
# ------------------------------------------------------------

# 3dpart.
#
# ------------------------------------------------------------

# blog.
from .models import Blog
from .models import Category

# config.
attrs_dict = { 'class': 'required' }

CATEGORY_CHOICES = {}
# ------------------------------------------------------------

class MyBlogAdminForm(forms.ModelForm):
    content   = forms.CharField(label=_(u"Content"),required=True)
    class Meta:
        model = Blog

class CreateBlogForm(forms.ModelForm):

    username = forms.RegexField(regex=r'^\w+$',
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=_(u'username'))
    title = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)),
                             label=_(u'title'))

    category = forms.ChoiceField(label=_(u'category'), choices=CATEGORY_CHOICES)

    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs=attrs_dict),
                                label=_(u'datetime'))

    content = forms.CharField(label=_(u'content'))
    slug          = forms.SlugField(label=_(u'Slug'),help_text="Use English Or Pinyin.")
    summary       = forms.CharField(label=_(u'Summary'),help_text="One paragraph. Don't add tag.")
    tags          = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,maxlength=75)), label=_(u'tags'))

    class Meta:
        model = Blog
