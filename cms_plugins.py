# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext as _

from .models import GalleryPluginModel
from .models import StartImage
from .models import ContactPage


class GalleryPlugin(CMSPluginBase):

    model = GalleryPluginModel
    name = _("Gallerie")
    render_template = "djangocms_gallerij/_gallery.html"

    def render(self, context, instance, placeholder):
        images = instance.gallery.images.all()
        context.update({
            'gallery': instance.gallery.name,
            'images': images
        })

        return context


class StartSliderPlugin(CMSPluginBase):

    model = GalleryPluginModel
    name = _("Start Slider")
    render_template = "djangocms_gallerij/_start_image_slider.html"

    def render(self, context, instance, placeholder):
        images = instance.gallery.images.all()
        context.update({
            'image_list': list(images),
            'start_slide': 0,
        })

        return context


class StartImagePlugin(CMSPluginBase):

    model = StartImage
    name = _("Start Bild")
    render_template = "djangocms_gallerij/_start_image.html"

    def render(self, context, instance, placeholder):
        image = instance.image
        context.update({
            'image': image,
        })

        return context


class ContactImagePlugin(CMSPluginBase):

    model = StartImage
    name = _("Contact Image")
    render_template = "djangocms_gallerij/_info_image.html"

    def render(self, context, instance, placeholder):
        image = instance.image
        context.update({
            'image': image,
        })

        return context


class ContactPagePlugin(CMSPluginBase):

    model = ContactPage
    name = _("Contact Page")
    render_template = "djangocms_gallerij/_contact_page.html"

    def render(self, context, instance, placeholder):
        image = instance.background_image
        text = instance.contact_text
        context.update({
            'image': image,
            'text': text,
        })

        return context

plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(StartImagePlugin)
plugin_pool.register_plugin(ContactImagePlugin)
plugin_pool.register_plugin(ContactPagePlugin)
