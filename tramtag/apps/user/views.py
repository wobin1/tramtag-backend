from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from django.http import Http404
from apps.utils.utilities import Utility


class TramtagUser(APIView):

    def post(self, request):
        request_data = request.data

        serializer = UserSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # generating token
        token = Utility.generate_token(self, request_data["email"])

        # sending email using the send email utility class
        Utility.send_email(self, request_data["email"], f"Click on the link to verify your account {token}", "Account Verification")

        response = Utility.get_response(self, "success", "Users created successfully!!!", serializer.data, status.HTTP_200_OK)

        return response

    def get(self, request):
        user = CustomUser.objects.all()

        serializer = UserSerializer(user, many=True)

        response = Utility.get_response(self, "success", "Users fetched!!!", serializer.data, status.HTTP_200_OK)

        return response

class SingleUser(APIView):

    def get(self, request, id):

        user = Utility().verify_user_id(id)

     
        serializer = UserSerializer(user)

        response = Utility.get_response("success", "User fetched!!!", serializer.data, status.HTTP_200_OK)

        return response   


    def put(self, request, id):
        request_data = request.data
        user = Utility().verify_user_id(id)

        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        response = Utility.get_response("success", "User Updated!!!", serializer.data, status.HTTP_200_OK)

        return response


    def delete(self, request, id):
        user = Utility().verify_user_id(id)

        user.delete()

        response = Utility.get_response("success", "User Deleted!!!", "No data", status.HTTP_200_OK)


        return response

        



