from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from logconfig.logger import get_logger
from user.models import User
from user.serializers import RegistrationSerializer

logger = get_logger()


# Create your views here.
class UserRegistration(APIView):
    serializer_class = RegistrationSerializer
    """
      class used to register for the user
    """

    def post(self, request):
        """
            this method is used to create the user for the registration
        """
        try:
            serializer = RegistrationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "User Registration Successfully", "status": 201, "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
            this method is used to retrieve the all registered users data
        """
        try:
            user = User.objects.all()
            serializer = RegistrationSerializer(user, many=True)
            return Response({"message": "Retrieve Data  Successfully", "status": 200, "data": serializer.data},
                            status=status.HTTP_200)
        except Exception as e:
            logger.exception(e)
        return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)
