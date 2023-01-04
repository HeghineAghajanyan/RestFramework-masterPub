# Python
from datetime import datetime
from urllib.request import Request

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

    def create(self, request: Request, format=None) -> Response:

        serializer: TempEntitySerializer = \
            TempEntitySerializer(
                data=request.data
            )

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был создан',
                    'payload': request.data
                }
            )
        serializer.save()

        return self.get_json_response(
            {
                'message': 'Объект был создан',
            }
        )

    def update(self, request: Request, pk: str) -> Response:

        obj: TempModel = self.get_obj_or_raise(
            self.queryset,
            pk
        )

        request.data._mutable = True
        print(obj)
        serializer: TempEntitySerializer = \
            TempEntitySerializer(
                obj,
                data=request.data
            )
        request.data['obj_id'] = obj.id
        print(request.data)
        print(serializer)
        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был обновлен',
                    'payload': request.data
                }
            )

        serializer.save()

        request.data._mutable = False

        return self.get_json_response(
            {
                'message': 'Объект был обновлен',
                'payload': request.data
            }
        )

    def partial_update(self, request: Request, pk: str) -> Response:

        obj: TempModel = self.get_obj_or_raise(
            self.queryset,
            pk
        )
        serializer: TempSerializer = \
            TempSerializer(
                obj,
                data=request.data,
                partial=True
            )
        request.data['obj_id'] = obj.id

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был частично-обновлен',
                    'payload': request.data
                }
            )

        serializer.save()

        return self.get_json_response(
            {
                'message': 'Объект был частично-обновлен',
                'payload': request.data
            }
        )

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
