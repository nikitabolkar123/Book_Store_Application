from rest_framework import serializers

from book.models import Book
from cart.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    # book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    # quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id', 'book', 'cart', 'quantity']
        read_only_field = ['cart']


class CartSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), write_only=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'total_quantity', 'total_price', 'status', 'book', 'quantity']
        # read_only_field=['status','total_price','total_quantity','user','quantity','book']

    def create(self, validated_data):
        user = validated_data.get('user')
        book = validated_data.get('book')
        quantity = validated_data.get('quantity')
        c_item = 0
        cart = Cart.objects.filter(user=user.id, status='unordered')
        if cart.exists():
            cart = cart.first()
            # cart.status = ''
            # cart.status = 'ordered'

            cart_item = CartItem.objects.filter(cart_id=cart.id, book_id=book.id)
            if cart_item.exists():
                cart_item = cart_item.first()
                cart_item.quantity += quantity
                c_item += cart_item.quantity
            else:
                cart_items = CartItem.objects.create(cart_id=cart.id, book_id=book.id, quantity=quantity)
                c_item += quantity
            total_book_price = book.price * c_item
            cart.total_price += total_book_price
            cart.total_quantity += c_item
            cart.save()
        else:
            # cart = Cart.objects.create(user_id=user.id, status='ordered')
            cart = Cart.objects.create(user_id=user.id)
            print(cart)
            cart_items = CartItem.objects.create(cart_id=cart.id, book_id=book.id, quantity=quantity)
            total_book_price = book.price * quantity
            cart.total_price += total_book_price
            cart.total_quantity += quantity
            cart_items.save()
        return cart
