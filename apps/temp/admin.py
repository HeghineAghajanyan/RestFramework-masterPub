from django.contrib import admin
from apps.temp.models import TempModel, TempEntity


class TempModelAdmin(admin.ModelAdmin):
    """TempModelAdmin."""

    readonly_fields = (
        'name',
        'number',
        'is_activated',
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


class TempEntityModelAdmin(admin.ModelAdmin):
    """TempModelAdmin."""

    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )


admin.site.register(
    TempModel, TempModelAdmin
)

admin.site.register(TempEntity, TempEntityModelAdmin)