from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from base.models import Post, PostImage


class IndexView(TemplateView):
    template_name = "base/index.html"


class InteriorsView(ListView):
    template_name = "base/interiors.html"
    model = Post
    context_object_name = "posts"


class InteriorView(DetailView):
    template_name = "base/interior.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = context["object"]
        photos = PostImage.objects.filter(post=post)
        context["post"] = post
        context["photos"] = photos
        context["range"] = range(1, len(photos))
        # print(photos[0].images.url)
        return context


class AboutUsView(TemplateView):
    template_name = "base/aboutus.html"


class MediaView(TemplateView):
    template_name = "base/media.html"
