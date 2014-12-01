from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from filer.models.filemodels import File
from .models import Gallery
from .models import Image


def image_slider(request, img_id):
    image = Image.objects.filter(pk=img_id)[0]
    image_gallery = image.gallery_id
    image_list = Image.objects.filter(gallery_id=image_gallery)
    image_list = list(image_list)
    start_slide = image_list.index(image)
    image_data = {}
    image_data['img_id'] = img_id
    image_data['image_list'] = image_list
    image_data['start_slide'] = start_slide
    return render(request, 'djangocms_gallerij/_image_slider.html', image_data)
