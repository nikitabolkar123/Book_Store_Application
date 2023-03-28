from rest_framework.response import Response
from rest_framework.views import APIView

from cart_app.models import UserCart, UserCartItem
from cart_app.serializers import CartItemSerializer, CartSerializer
from logconfig.logger import get_logger

logger = get_logger()


# Create your views here.

class CartItemAPI(APIView):

    def post(self, request):
        try:
            request.data.update({"user": request.user.id})
            serializer = CartItemSerializer(data=request.data, context={"user": request.user})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Cart Item Added Successfully', "status": 201, 'data': serializer.data},
                            status=201)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e), 'status': 400}, status=400)

    def get(self, request, cart_id):
        try:
            cart = UserCart.objects.get(id=cart_id)
            print(cart.cart_items.filter(cart_id=cart_id))
            cart_serializer = CartSerializer(cart, many=False)
            return Response({"Message": "List of Cart Items",
                             "data": cart_serializer.data,
                             "status": 200})

        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e)}, status=400)

    def delete(self, request, cart_item_id):
        try:
            cart_item = UserCartItem.objects.get(id=cart_item_id)
            cart_item.delete()
            return Response({"Message": "Cart Item Deleted Successfully", "status": 204})
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e)}, status=400)


class CheckoutAPI(APIView):

    def put(self, request):
        print(request.user.id)
        user = UserCart.objects.get(user_id=request.user.id, status=False)
        if user is not None:
            user.status = True
            user.save()
        return Response({"Message": "status updated Successfully", 'status': 200})

    def get(self, request):
        try:
            cart = UserCartItem.objects.all()
            serializer = CartItemSerializer(many=True)
            return Response({'message': 'Book data retrieved successfully', 'data': serializer.data, 'status': 200},
                            status=200)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=400)
