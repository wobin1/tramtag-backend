from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.utils.utilities import Utility
from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.models import CustomUser
from apps.user.serializers import UserSerializer
from apps.user.views import SingleUser
from django.conf import settings

        


class UserAuthentication(APIView): 

    # this function is generating tokens
    # it returns the generated tokens
    def get_token(self, user):
        # generating token
        token = RefreshToken.for_user(user)

        tokens = { 'access_token': str(token.access_token), 'refresh': str(token)}

        return tokens
           
        
    # this code facilitate login
    def post(self, request):
        # geting client data
        request_data = request.data

        email = request_data['email']
        password = request_data['password']

        # checking if email exist in client data
        if email is None or not password:
            print("email or password absent")
            response = Utility.get_response(self, "error", "Please provide email and password!!!", "no data", status.HTTP_404_NOT_FOUND)


        # checking if user exist in Database
        try:
            user = CustomUser.objects.get(email=email)

            # checking if password is correct
            if not user.check_password(password):
                response = Utility.get_response(self, "error", "Invalid Password!!!", "no data", status.HTTP_404_NOT_FOUND)
                return response
            
        except CustomUser.DoesNotExist:
            response = Utility.get_response(self, "error", "Invalid Email", "no data", status.HTTP_404_NOT_FOUND)
            return response
            

        # getting user data
        
        serializer = UserSerializer(user)

        user_data = {
            "user_id": serializer.data["id"],
            "user_email": serializer.data["email"],
            "tokens": self.get_token(user)
        }

        response = Utility.get_response(self, "success", "login successfull", user_data, status.HTTP_200_OK)


        return response

class UserVerification(APIView):
    
    def get(self, request, token):
        
        # decoding token
        decode_token = Utility.decode_token(self, token)
        print(decode_token)

        if decode_token:
            verify_user = Utility.verify_user_email(self, decode_token["email"])
        else:
            response = Utility.get_response(self, "error", "Invalid User", "no data", status.HTTP_400_BAD_REQUEST)
            return response  

        if verify_user:
            response = Utility.get_response(self, "success", "User verified", "no data", status.HTTP_200_OK)
            return response
        if not verify_user:
            response = Utility.get_response(self, "error", "Invalid user", "no data", status.HTTP_404_NOT_FOUND)
            return response


class ForgotPassword(APIView):

    # This code is sending a password resset link
    def post(self, request):
        request_data = request.data
        email = request_data["email"]

        # checking user
        user = Utility.verify_user_email(self, email)

        # generating token
        if user:
            token = Utility.generate_token(self, email)
        else:
            response = Utility.get_response(self, "error", f"User with email {email} not found!!!", "no data", status.HTTP_404_NOT_FOUND)
            return response

        # sending email using the send email utility class
        Utility.send_email(self, email, f"Click on the link to reset your password {token}", "Reset Password")

        response = Utility.get_response(self, "success", "An a password reset link has been sent to the email.", token, status.HTTP_200_OK)
        return response


class ResetPassword(APIView):

    def confirm_password(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False


    def post(self, request, token):
        request_data = request.data
        
        password_confirm = self.confirm_password(request_data["password"], request_data["confirm_password"])

        # confirming both client data is valid  
        if password_confirm:
            # decoding token
            token_decode = Utility.decode_token(self, token)
            print(token_decode)

            user = CustomUser.objects.get(email=token_decode["email"])

            # hashing new password
            try:
                user.set_password(request.data["password"])
                user.save()

                user_serializer = UserSerializer(user).data
            except Exception as e:
                response = Utility.get_response(self, "error", "There was a problem updating user password.","no data", status.HTTP_400_BAD_REQUEST)
                return response

        response = Utility.get_response(self, "success", "User Updated Successfully.", user_serializer, status.HTTP_200_OK)
        return response
          

class TokenRefresh(APIView):

    def post(self, request):
        request_data = request.data

        refresh_token = request_data["refresh_token"]

        # checking if client data is not empty
        if refresh_token is None:
            response = Utility.get_response(self, "error", "please provide refresh token", "no data", status.HTTP_404_NOT_FOUND)
            return response

        # verifying token validity
        try:
            token = RefreshToken(refresh_token)
        except Exception as e:
            response = Utility.get_response(self, "error", str(e), "no data", status.HTTP_404_NOT_FOUND)
            return response

        new_token = {'access_token': str(token.access_token), 'refresh': str(token)}

        response = Utility.get_response(self, "success", "Token refreshed successfully", new_token, status.HTTP_200_OK)
        return response

