# DRF
from rest_framework.serializers import (
    BooleanField,
    CharField,
    IntegerField,
    ModelSerializer
)

# Local
from .models import (
    TempEntity,
    TempModel
)


class TempSerializer(ModelSerializer):
    name = CharField(required=False)
    number = IntegerField(required=False)
    is_activated = BooleanField(required=False)

    class Meta:
        model = TempModel
        fields = (
            'id',
            'name',
            'number',
            'is_activated'
        )


class TempEntitySerializer(ModelSerializer):
    firstname = CharField(
      required=True
    )

    lastname = CharField(
        required=True
    )
    phone_number = IntegerField(
        required=True
    )

    apartment_number = IntegerField(
        required=True
    )

    has_paid_taxes = BooleanField(
        required=True
    )

    class Meta:
        model = TempEntity
        fields = (
            'id',
            'firstname',
            'lastname',
            'phone_number',
            'apartment_number',
            'has_paid_taxes'
        )
