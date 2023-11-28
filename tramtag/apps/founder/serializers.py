from rest_framework import serializers
from .models import Founder



class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
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
            return founder