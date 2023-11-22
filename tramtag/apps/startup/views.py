from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Startup, Founders
from .serializers import StartupSerializer, FounderSerializer
from datetime import datetime
from apps.utils.utilities import Utility


class Startup(APIView):
    def post(self, request):
        request_data = request.data

        serializer = StartupSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        response = Utility.get_response(
            self,
            "success",
            "Startup created successfully!!!",
            serializer.data,
            status.HTTP_200_OK,
        )

        return response

    def get(self, request):
        user = CustomUser.objects.all()

        serializer = UserSerializer(user, many=True)

        response = Utility.get_response(
            self, "success", "Users fetched!!!", serializer.data, status.HTTP_200_OK
        )

        return response
