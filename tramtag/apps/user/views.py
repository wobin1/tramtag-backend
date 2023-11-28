from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from django.http import Http404
from apps.utils.utilities import Utility
from apps.utils.request_helper import RequestHelper



class TramtagUser(APIView):
    def post(self, request):
        request_data = request.data

        if request_data["password"] != request_data["confirm_password"]:
            return Response({"error": "password do not match"}, status=status.HTTP_400_BAD_REQUEST)

        
        serializer = UserSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


        # generating token
        token = Utility.generate_token(self, request_data["email"])

        # sending email using the send email utility class
        Utility.send_email(
            self,
            request_data["email"],
            f"Click on the link to verify your account {token}",
            "Account Verification",
        )

        response = Utility.get_response(
            self,
            "success",
            "Users created successfully!!!",
            serializer.data,
            status.HTTP_200_OK,
        )

        return response

    def get(self, request):
        user = CustomUser.objects.all()

        request_response = RequestHelper.get_object(self, user, UserSerializer, "user fetched!!!")

        return request_response


class SingleUser(APIView):
    def get(self, request, id):
        user = Utility().verify_id(id, CustomUser)

        request_response = RequestHelper.get_object_detail(self, user, UserSerializer, "user fetched!!!")

        return request_response

    def put(self, request, id):
        request_data = request.data
        user = Utility().verify_id(id, CustomUser)

        request_response = RequestHelper.put_object_update(self, user, request_data, UserSerializer, "user updated!!!")

        return request_response

    def delete(self, request, id):
        user = Utility().verify_id(id, CustomUser)

        request_response = RequestHelper.delete_object_delete(self, user, "user deleted!!!")

        return request_response
