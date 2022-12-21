from datetime import datetime

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.temp.models import TempModel, TempEntity
from apps.temp.serializers import TempSerializer, TempEntitySerializer


class TempViewSet(ViewSet):
    queryset = TempModel.objects.all()

    def list(self, request, format=None) -> Response:
        serializer = TempSerializer(self.queryset, many=True)
        return Response(serializer.data)


class TempEntityViewSet(ViewSet):
    queryset = TempEntity.objects.all()

    def list(self, request, format=None) -> Response:
        serializer = TempEntitySerializer(self.queryset.get_not_deleted(), many=True)
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