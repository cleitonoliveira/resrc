# -*- coding: utf-8 -*-:
from django.shortcuts import get_object_or_404, redirect

from taggit.models import Tag

from resrc.utils import render_template
from resrc.link.models import Link


def single(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)

    links = Link.objects.filter(tags=tag)

    return render_template('tags/show_single.html', {
        'tag': tag,
        'links': links,
        'request': request,
    })


def index(request):
    from django.db.models import Count
    tags = Tag.objects.select_related('links') \
        .annotate(c=Count('link')).order_by('-c', 'name') \
        .exclude(name=None) \
        .all()
    tags = list(tags)

    return render_template('tags/show_index.html', {
        'tags' : tags
    })


def search(request, tags):
    t2 = tags.split('-')
    t2 = [t.split('&') for t in t2]
    #t2 = [t.split('|') for t in t2]
    print t2
