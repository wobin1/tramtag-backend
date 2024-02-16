from rest_framework import serializers
from .models import Startup


class StartupSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        model = Startup
        fields = [
            "id",
            "startup_name",
            "startup_email",
            "startup_location",
            "startup_industry",
            "startup_description",
            "startup_website_url",
            "startup_phone_number",
            "startup_linkedin_profile",
            "founded_in",
            "founders",
            "additional_info",
        ]


        def create(self, validated_data):
            startup = Startup(
                startup_name = validated_data["startup_name"],
                startup_email = validated_data["startup_email"],
                startup_location = validated_data["startup_location"],
                startup_industry = validated_data["startup_industry"],
                startup_linkedin_profile = validated_data["startup_linkedin"],
                startup_phone_number = validated_data["phone_number"],
                StartupSerializer = validated_data["phone_number"],
                startup_description = validated_data["startup_description"],
                startup_website_url = validated_data["startup_website_url"],
                founders = validated_data["founders"],
                additional_info = validate_data["additional_info"]
                
            )

            startup.save()
            return startup


