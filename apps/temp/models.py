# Django
import datetime

from django.db import models
from django.db.models import (
    F,
    QuerySet
)

# First party
from abstracts.models import AbstractsDateTime
from temp.validators import TempModelValidator


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


class TempEntity(AbstractsDateTime, TempModelValidator):
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

    # def clean(self) -> None:
    #     self.validate_number(
    #         self.number
    #     )

    def clean(self) -> None:
        self.validate_apartment_number(
            self.apartment_number
        )
        self.validate_firstname(self.firstname)

# TODO: here we can send_email
    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_delete = datetime.datetime.now()
        self.save(update_field=['datetime_deleted'])
