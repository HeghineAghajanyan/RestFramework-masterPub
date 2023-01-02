# Python
from datetime import datetime

# DRF
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from abstracts.mixins import ResponseMixin, ValidationMixin

# Local
from .models import (
    TempEntity,
    TempModel
)
from .serializers import (
    TempEntitySerializer,
    TempSerializer,
    TempTwoSerializer,
)


class TempViewSet(ResponseMixin, ViewSet):
    queryset = TempModel.objects.all()

    def list(self, request, format=None) -> Response:
        serializer = TempSerializer(self.queryset, many=True)
        return self.get_json_data(serializer.data)


class TempEntityViewSet(ResponseMixin, ValidationMixin, ViewSet):
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
        serializer = TempTwoSerializer(
            self.queryset.get_not_deleted(),
            many=True
        )
        return self.get_json_response(serializer.data)

    def list(self, request: Response) -> Response:
        serializer: TempEntitySerializer = TempEntitySerializer(self.queryset.get_not_deleted(), many=True)
        return self.get_json_response(serializer.data)


    def retrieve(self, request: Response, pk) -> Response:
        obj = self.get_obj_or_raise(self.queryset, pk)
        serializer = TempSerializer(obj)
        return self.get_json_response(serializer.data)

    def destroy(self, request, pk: str) -> Response:
        obj = self.get_obj_or_raise(self.queryset, pk)
        obj.delete()

        return self.get_json_response({
                'message': 'Object was deleted',
                'object_id': f'{obj.id}',
                'object_deleted': f'{obj.datetime_deleted}',
            })
