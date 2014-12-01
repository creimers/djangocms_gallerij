from django.db import models
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey

from filer.fields.image import FilerImageField


class Gallery(models.Model):

    name = models.CharField(max_length=50)

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
