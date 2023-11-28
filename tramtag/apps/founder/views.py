from rest_framework.views import APIView
from rest_framework import status
from .models import Founder
from .serializers import FounderSerializer
from apps.utils.utilities import Utility
from apps.utils.request_helper import RequestHelper


class FounderView(APIView):

    def post(self, request):
        request_data = request.data

        request_response = RequestHelper.post_object(self, request_data, FounderSerializer, "founder created!!!")

        return request_response


    def get(self, request):

        founder = Founder.objects.all()

        request_response = RequestHelper.get_object(self, founder, FounderSerializer, "founder fetched!!!")

        return request_response


class SingleFounderView(APIView):
    
    def get(self, request, id):

        try:
            founder = Utility.verify_id(self, id, Founder)

            request_response = RequestHelper.get_object_detail(self, founder, FounderSerializer, "founder fetched!!!")

            return request_response
        except Exception as e:
            print(str(e))
            request_response = Utility.get_response(self, "error", "Founder not found", "no data", status.HTTP_404_NOT_FOUND)

            return request_response


    def put(self, request, id):
        request_data = request.data

        try:
            founder = Utility.verify_id(self, id, Founder)
            print(founder)
            request_response = RequestHelper.put_object_update(self, founder, request_data, FounderSerializer, "founder updated!!!")

            return request_response
        except Exception as e:
            print(str(e))
            request_response = Utility.get_response(self, "error", "Founder not found", "no data", status.HTTP_404_NOT_FOUND)

            return request_response



    def delete(self, request, id):
        try:
            founder = Utility.verify_id(self, id, Founder)

            request_response = RequestHelper.delete_object_delete(self, founder, "founder deleted!!!")

            return request_response
        except Exception as e:
            print(str(e))
            request_response = Utility.get_response(self, "error", "Founder not found", "no data", status.HTTP_404_NOT_FOUND)

            return request_response