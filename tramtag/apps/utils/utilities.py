from rest_framework.response import Response
from rest_framework import status
from apps.user.models import CustomUser
from django.http import Http404
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import jwt


class Utility:

    def get_response(self, status, message, data, status_code):
        status= status_code,
        message= message,
        data= data
        status= status_code

        response_data = Response({
            "status": status,
            "message": message,
            "data": data
        }, status= status_code)

        return response_data

    def verify_user_id(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    # This code is verifying the users' email
    def verify_user_email(self, email):
        print("verifying email")
        try:
            user = CustomUser.objects.get(email=email)
            print("verified User:", user)
            return user.id
        except CustomUser.DoesNotExist:
            raise Http404

        print("verification done!")

    def send_email(self, email_address, email_content, subject):
        # This code is sending email and allowing me to pass a html content
        subject, from_email, to = subject, "settings.EMAIL_HOST_USER", email_address
        text_content = ""
        html_content = f"<p>Click on the link below to reset your password <br> <strong><a>{email_content}</a>  </strong></p>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        print("email sent")

        # response = self.get_response("success", f"Email sent to {email_address}", "no data", status.HTTP_200_OK)

        return Response({"message": "email sent"})

    # this code generates jwt token
    def generate_token(self, user_email):
        key = settings.SECRET_KEY
        # generating token
        token = jwt.encode({"email": user_email}, key, algorithm="HS256")

        print("token generated!")

        return token

    # this code decodes jwt token
    def decode_token(self, token):
        key = settings.SECRET_KEY

        try:
            payload = jwt.decode(token, key, algorithms=["HS256"])
            print("token decoded!")
            return payload
            
        except Exception as e:
            print(str(e))
            raise Http404

        