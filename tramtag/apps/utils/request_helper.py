from apps.utils.utilities import Utility
from rest_framework import status
from rest_framework.response import Response




class RequestHelper:

    # this code facilitate the saving of objects to the database
    def post_object(self, request_data:dict, serializer_name, message:str):
        object_serializer = serializer_name(data=request_data)
        if object_serializer.is_valid(raise_exception=True):
            object_serializer.save()

        response = Utility.get_response(
            self,
            "success",
            message,
            object_serializer.data,
            status.HTTP_200_OK,
        )
        return response


    # this code facilitates the get request to fect objects
    def get_object(self, object, serializer_name, message):

        serializer = serializer_name(object, many=True)

        response = Utility.get_response(
            self, "success", message, serializer.data, status.HTTP_200_OK
        )

        return response


    # this code facilitate the get request to fetch the details of an object
    def get_object_detail(self, object, serializer_name, message):
        if object:
            serializer = serializer_name(object)
        
        response = Utility.get_response(
        self, "success", message, serializer.data, status.HTTP_200_OK
        )
        return response


    # this code facilitate the put request to update an object data
    def put_object_update(self, object, request_data, serializer_name, message):

        object_serializer = serializer_name(object, data=request_data)
        if object_serializer.is_valid(raise_exception=True):
            object_serializer.save()

        response = Utility.get_response(self, "success", message, object_serializer.data, status.HTTP_200_OK)

        return response

    # this code facilitate object delete
    def delete_object_delete(self, object, message):
        object.delete()

        response = Utility.get_response(self, "success", message, "No data", status.HTTP_200_OK)


        return response