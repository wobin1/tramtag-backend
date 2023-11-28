from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Startup
from .serializers import StartupSerializer
from apps.utils.utilities import Utility
from apps.utils.request_helper import RequestHelper


class StartupView(APIView):
    def post(self, request):
        request_data = request.data

        request_response = RequestHelper.post_object(
            self, request_data, StartupSerializer, "Startup created successfully!!!"
        )
        print(request_response)
        return request_response

    def get(self, request):
        startup = Startup.objects.all()

        request_response = RequestHelper.get_object(
            self, startup, StartupSerializer, "Startups fetched!!!"
        )

        return request_response


class SingleStartupView(APIView):
    def get(self, request, id):
        try:
            startup = Utility.verify_id(self, id, Startup)
            print(startup)
        except Exception as e:
            print(str(e))
            response = Utility.get_response(self, "error", "invalid startup ID", "No data", status.HTTP_400_BAD_REQUEST)
            return response

        request_response = RequestHelper.get_object_detail(
            self, startup, StartupSerializer, "Startup fetched!!!"
        )

        return request_response

    def put(self, request, id):
        request_data = request.data
        startup = Utility().verify_id(id, Startup)

        request_response = RequestHelper.put_object_update(
            self, startup, request_data, StartupSerializer, "Startup Updated!!!"
        )

        return request_response

    def delete(self, request, id):
        startup = Utility().verify_id(id, Startup)

        request_response = RequestHelper.delete_object_delete(
            self, startup, "startup deleted!!!"
        )

        return request_response
