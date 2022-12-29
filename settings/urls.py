# DRF
from rest_framework.routers import DefaultRouter

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path
)

# First party
from temp.views import (
    TempEntityViewSet,
    TempViewSet
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls'))
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('temp', TempViewSet, basename='temper')
router.register('temp2', TempEntityViewSet, basename='tempEntity')

urlpatterns += [
    path(
        'api/v1/',
        include(router.urls)
    )
]
