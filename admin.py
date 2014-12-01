from django.contrib import admin

from djangocms_gallerij.models import Gallery
from djangocms_gallerij.models import Image

from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline


class GalleryImageInline(SortableStackedInline):
    model = Image
    extra = 1


class GalleryAdmin(NonSortableParentAdmin):
    inlines = [GalleryImageInline, ]


admin.site.register(Gallery, GalleryAdmin)
