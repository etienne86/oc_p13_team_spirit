"""Contain the models related to the app ``profiles``."""

from django.db import models


from teamspirit.catalogs.managers import (
    CatalogManager,
    ProductManager,
)


class Catalog(models.Model):
    """Contain catalog information."""

    name = models.CharField(
        max_length=50,
        verbose_name='Nom du catalogue',
        null=False,
        blank=False,
        default='(catalogue sans nom)',
    )

    objects = CatalogManager()



class Product(models.Model):
    """Contain product information."""

    name = models.CharField(
        max_length=50,
        verbose_name='Article',
        null=False,
        blank=False,
        default='(produit sans nom)',
    )
    image = models.FileField(
        null=True,
        blank=True,
        verbose_name='Photo',
        upload_to='produits/',
    )
    size = models.CharField(
        max_length=5,
        verbose_name='Taille',
        null=False,
        blank=False,
        default='(produit sans taille)',
    )
    is_available = models.BooleanField(
        null=False,
        blank=False,
        default=True,
        verbose_name='Produit disponible ?',
    )
    is_free = models.BooleanField(
        null=False,
        blank=False,
        default=False,
        verbose_name='Produit offert ?',
    )
    price = models.IntegerField(
        verbose_name='Prix',
        null=True,
        blank=True,
        default=0,
    )
    catalog = models.ForeignKey(
        to=Catalog,
        on_delete=models.CASCADE,
        null=False,
    )

    objects = ProductManager()
