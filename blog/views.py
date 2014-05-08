# -*- coding: utf-8 -*-

# python.
# ------------------------------------------------------------

# django.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.views.generic import DetailView, ListView
# ------------------------------------------------------------

# 3dpart.
# ------------------------------------------------------------

# blog.
from .models import Blog
from .forms import CreateBlogForm
# ------------------------------------------------------------

# config.
# ------------------------------------------------------------

def index(request):
    qs = Blog.objects.all()
    return ListView.as_view(model=Blog, queryset=qs,paginate_by=10 )(request)

class BlogIndexView(ListView):
    model=Blog
    template_name='blog/index.html'

def post(request, success_url=None,
             form_class=CreateBlogForm,
             template_name='blog/blog_post.html',
             extra_context=None):

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = form.save(profile_callback=profile_callback)
            # success_url needs to be dynamically generated here; setting a
            # a default value using reverse() will cause circular-import
            # problems with the default URLConf for this application, which
            # imports this file.
            return HttpResponseRedirect(success_url or reverse('registration_complete'))
    else:
        form = form_class()

    if extra_context is None:
        extra_context = {}
    context = RequestContext(request)
    for key, value in extra_context.items():
        context[key] = callable(value) and value() or value
    return render_to_response(template_name,
                              { 'form': form,},
                              context_instance=context)


