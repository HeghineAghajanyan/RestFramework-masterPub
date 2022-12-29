# Django
from django.db import models
from django.db.models import (
    F,
    QuerySet
)

# First party
from abstracts.models import AbstractsDateTime


class TempModelQuerySet(QuerySet):
    """TempModelQuerySet."""

    def get_deleted(self):
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self):
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_not_equal_updated(self):
        return self.exclude(
            datetime_updated=F('datetime_created')
        )

    def get_obj(self, p_key: str):
        try:
            return self.get(
                id=p_key
            )
        except TempModel.DoesNotExist:
            return None


class TempModel(AbstractsDateTime):
    """TempModel."""

    name = models.CharField(
        verbose_name='имя',
        max_length=25
    )
    number = models.IntegerField(
        verbose_name='число',
    )
    is_activated = models.BooleanField(
        default=False
    )

    objects = TempModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'number',
        )


class TempEntity(AbstractsDateTime):
    """TempEntity."""

    firstname = models.CharField(
        verbose_name='firstname',
        max_length=25
    )

    lastname = models.CharField(
        verbose_name='lastname',
        max_length=25
    )
    phone_number = models.IntegerField(
        verbose_name='phone number',
    )

    apartment_number = models.IntegerField(
        verbose_name='apartment number',
    )

    has_paid_taxes = models.BooleanField(
        default=True
    )

    objects = TempModelQuerySet().as_manager()

    class Meta:
        ordering = (
            'lastname',
        )
