# Python
from datetime import datetime

# DRF
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Local
from .models import (
    TempEntity,
    TempModel
)
from .serializers import (
    TempEntitySerializer,
    TempSerializer
)


class TempViewSet(ViewSet):
    queryset = TempModel.objects.all()

    def list(self, request, format=None) -> Response:
        serializer = TempSerializer(self.queryset, many=True)
        return Response(serializer.data)


class TempEntityViewSet(ViewSet):
    queryset = TempEntity.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='list-2',
        permission_classes=(
            AllowAny,
        )
    )
    def list2(self, request, format=None) -> Response:
        serializer = TempEntitySerializer(
            self.queryset.get_not_deleted(),
            many=True
        )
        return Response(serializer.data)

    def destroy(self, request, pk: str) -> Response:
        obj = self.queryset.get(
            id=pk
        )
        obj.datetime_deleted = datetime.now()
        obj.save()

        return Response(
            {
                'message': 'Object was deleted',
                'object_id': f'{obj.id}',
                'object_deleted': f'{obj.datetime_deleted}',
            }
        )
