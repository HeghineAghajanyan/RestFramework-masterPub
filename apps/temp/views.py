from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic.detail import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.temp.models import TempModel
from rest_framework import status


class TempList(APIView):
    def get(self, request, format=None):
        return Response({'key':'value'})
