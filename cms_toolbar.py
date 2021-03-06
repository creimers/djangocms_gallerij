# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
# from cms.toolbar.items import Break, SubMenu
# from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK


@toolbar_pool.register
class GalleryToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            'djangocms_blog',
            _('Gallerien')
        )

        url = reverse('admin:djangocms_gallerij_gallery_changelist')
        admin_menu.add_modal_item(_('Gallerien'), url=url)
        url = reverse('admin:djangocms_gallerij_gallery_add')
        admin_menu.add_modal_item(_('Neue Gallerie'), url=url)
