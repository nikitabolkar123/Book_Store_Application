from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from cart.serializers import CartItemSerializer,CartSerializer
from cart.models  import Cart
from logconfig.logger import get_logger

logger = get_logger()


# Create your views here.

class CartItemViews(APIView):
    def post(self, request):
        try:
            request.data.update({'user':request.user.id})
            # cart=Cart.objects.create(user=request.user.id)
            # request.data.update({"cart":cart.id})
            serializer = CartSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'message': " Book Added to cart Successfully",
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=status.HTTP_400_BAD_REQUEST)

