# -*- coding: utf-8 -*-

# python.
#
# ------------------------------------------------------------

# django.
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django import forms
from django.utils.translation import ugettext_lazy as _
# ------------------------------------------------------------

# 3dpart.
#
# ------------------------------------------------------------

# blog.
from .models import Blog
from .models import Category
from .forms  import CreateBlogForm,MyBlogAdminForm
# ------------------------------------------------------------

class BlogAdmin(admin.ModelAdmin):
    #form = BlogBlogAdminForm
    form = MyBlogAdminForm

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change):
        def set_user(instance):
            instance.user = request.user
            instance.save()

        if formset.model == Comment:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

    #prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'user','category','pub_date')
    list_filter = ['pub_date']
    search_fields = ['title','user' ,'summary', 'content']
    date_hierarchy = 'pub_date'

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
