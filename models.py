from django.db import models
from cms.models import CMSPlugin

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey

from filer.fields.image import FilerImageField

from djangocms_text_ckeditor.fields import HTMLField


class Gallery(models.Model):

    name = models.CharField(max_length=50)

    def copy_relations(self, oldinstance):
        for image in oldinstance.images.all():
            image.pk = None
            image.social_list = self
            image.save()

    def __unicode__(self):
        return u'%s' % self.name


class Image(Sortable):
    class Meta(Sortable.Meta):
        pass

    gallery = SortableForeignKey(
        Gallery,
        related_name="images"
    )

    image = FilerImageField(
        null=True,
        blank=False
    )

    caption_text = models.CharField(
        null=True,
        blank=True,
        max_length=255
    )

    def __unicode__(self):
        if self.caption_text:
            return u'%s' % self.caption_text
        else:
            return u'%s' % self.image.label


class GalleryPluginModel(CMSPlugin):
    gallery = models.ForeignKey(Gallery)

    def __unicode__(self):
        return u'%s' % self.gallery.name


class StartImage(CMSPlugin):
    image = FilerImageField(
        null=True,
        blank=False
    )

    def __unicode__(self):
        return u'%s' % self.image.label


class ContactPage(CMSPlugin):
    background_image = FilerImageField(
        null=True,
        blank=False
    )
    contact_text = HTMLField(blank=True)

    def __unicode__(self):
        return u'%s' % self.background_image.label
