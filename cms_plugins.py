# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext as _

from .models import GalleryPluginModel


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

plugin_pool.register_plugin(GalleryPlugin)
