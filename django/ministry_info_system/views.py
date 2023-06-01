from multiprocessing import context
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView
from django.http import Http404
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from django.db.models import Q



from ministry_info_system.models import *

from django.http import JsonResponse, HttpResponse

class MedicalEnsuranceView(APIView):
    """
    Ukraine organizations.
    Retrieve, update or delete a organization instance.
    """
    authentication_classes = ()
    permission_classes = ()

    @swagger_auto_schema(
        responses={404: "NOT FOUND"}, )
    def get(self, request, format=None):
        """
        Retrieve organization by path id.
        """
        person_unique_code = request.GET.get('person_unique_code', None)

        person_lists = MedicalEnsurance.objects.filter(person_unique_code=person_unique_code)

        if person_lists.count() > 0:
            obj = person_lists.first()
            return JsonResponse({
                'status': 'success',
                'data': {
                    'ensurance_type': obj.ensurance_type,
                    'person_unique_code': obj.person_unique_code,
                    'person_fullname': obj.person_fullname,
                    'person_home_address': obj.person_home_address,
                    'person_medical_ensurance': obj.person_medical_ensurance,
                }
            })
        else:
            return JsonResponse({
                'status': 'failure',
                'error_text': 'Not found'
            })