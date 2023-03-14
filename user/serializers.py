from rest_framework import serializers
from logconfig.logger import get_logger
from user.models import User
logger = get_logger()

class RegistrationSerializer(serializers.ModelSerializer):
    """
       Serializer class used in DRF to convert objcet into bytes
    """
    class Meta:
        """
             meta class is used to change the behaviour of the model fields
        """
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'phone_no', 'password', 'location']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
               built in method for the serializer class to craete the db
        """
        return User.objects.create_user(**validated_data)
