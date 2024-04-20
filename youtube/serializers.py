from rest_framework import serializers
from .models import Video, APIAuthKey

class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model.
    """

    class Meta:
        model = Video
        fields = '__all__'

    def validate_title(self, value):
        """
        Validate the title field to ensure it is not empty.
        """
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        """
        Validate the description field to ensure it is not empty.
        """
        if not value:
            raise serializers.ValidationError("Description cannot be empty.")
        return value

class APIAuthKeySerializer(serializers.ModelSerializer):
    """
    Serializer for the APIAuthKey model.
    """

    class Meta:
        model = APIAuthKey
        fields = '__all__'

    def validate_auth_key(self, value):
        """
        Validate the auth_key field to ensure it is not empty.
        """
        if not value:
            raise serializers.ValidationError("Auth key cannot be empty.")
        return value
