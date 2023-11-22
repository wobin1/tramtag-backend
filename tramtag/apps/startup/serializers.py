from rest_framework import serializers
from .models import Startup


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = [
            "id",
            "startup_name",
            "startup_location",
            "startup_industry",
            "startup_description",
            "founded_in"
        ]


        def create(self, validated_data):
            startup = Startup(
                startup_name = validated_data["startup_name"],
                startup_location = validated_data["startup_location"],
                startup_industry = validated_data["startup_industry"],
                startup_description = validated_data["startup_description"]
            )

            startup.save()
            return alawi


class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = [
            "id",
            "startup_id",
            "founder_first_name",
            "founder_last_name",
            "founder_email"
        ]


        def create(self, validated_data):
            founder = Startup(
                startup_id = validated_data["startup_name"],
                founder_first_name = validated_data["startup_location"],
                founder_last_name = validated_data["startup_industry"],
                founder_email = validated_data["startup_description"]
            )

            founder.save()
            return alawi