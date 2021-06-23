from saleor.store.models import Store
from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel

from ..core.models import ModelWithMetadata, MultitenantModelWithMetadata, SortableModel
from ..core.permissions import MenuPermissions
from ..core.utils.translations import TranslationProxy
from ..page.models import Page
from ..product.models import Category, Collection


class Menu(MultitenantModelWithMetadata):
    store = models.ForeignKey(
        Store,
        related_name="menus",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tenant_id='store_id'
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)

    class Meta(MultitenantModelWithMetadata.Meta):
        ordering = ("pk",)
        permissions = ((MenuPermissions.MANAGE_MENUS.codename, "Manage navigation."),)

    def __str__(self):
        return self.name


class MenuItem(MultitenantModelWithMetadata, MPTTModel, SortableModel):
    store = models.ForeignKey(
        Store,
        related_name="items",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tenant_id='store_id'
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    # not mandatory fields, usage depends on what type of link is stored
    url = models.URLField(max_length=256, blank=True, null=True)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.CASCADE
    )
    collection = models.ForeignKey(
        Collection, blank=True, null=True, on_delete=models.CASCADE
    )
    page = models.ForeignKey(Page, blank=True, null=True, on_delete=models.CASCADE)

    tree = TreeManager()
    translated = TranslationProxy()

    class Meta(MultitenantModelWithMetadata.Meta):
        ordering = ("sort_order", "pk")
        app_label = "menu"

    def __str__(self):
        return self.name

    def get_ordering_queryset(self):
        return (
            self.menu.items.filter(level=0)
            if not self.parent
            else self.parent.children.all()
        )

    @property
    def linked_object(self):
        return self.category or self.collection or self.page


class MenuItemTranslation(models.Model):
    language_code = models.CharField(max_length=10)
    menu_item = models.ForeignKey(
        MenuItem, related_name="translations", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)

    class Meta:
        ordering = ("language_code", "menu_item", "pk")
        unique_together = (("language_code", "menu_item"),)

    def __repr__(self):
        class_ = type(self)
        return "%s(pk=%r, name=%r, menu_item_pk=%r)" % (
            class_.__name__,
            self.pk,
            self.name,
            self.menu_item_id,
        )

    def __str__(self):
        return self.name
