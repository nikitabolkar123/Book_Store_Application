from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from book.models import Book
from book.serializers import BookSerializer
from logconfig.logger import get_logger

logger = get_logger()


class BookAPIViews(APIView):
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BookSerializer, operation_summary='POST BOOK')  # automatically generated open api
    def post(self, request):
        if not request.user.is_superuser:
            return Response({'message': 'You do not have permission to create a new book'}, status=403)
        try:
            request.data.update({'user': request.user.id})
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Book created successfully', 'data': serializer.data, 'status': 201},
                            status=201)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=400)

    @swagger_auto_schema(operation_summary='GET BOOK')
    def get(self, request):
        try:
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response({'message': 'Book data retrieved successfully', 'data': serializer.data, 'status': 200},
                            status=200)
        except Exception as e:
            logger.exception(e)
            return Response({'message': str(e)}, status=400)

    @swagger_auto_schema(request_body=BookSerializer, operation_summary='PUT BOOK')
    def put(self, request, book_id):
        if not request.user.is_superuser:
            return Response({'message': 'You do not have permission to update book'}, status=403)
        try:
            request.data.update({'user': request.user.id})  #
            books = Book.objects.get(id=book_id)
            serializer = BookSerializer(books, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Book Updated Successfully", "status": 200, "data": serializer.data},
                            status=200)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)

    @swagger_auto_schema(request_body=BookSerializer, operation_summary='DELETE BOOK')
    def delete(self, request, book_id):
        if not request.user.is_superuser:
            return Response({'message': 'You do not have permission to delete book'}, status=403)
        try:
            books = Book.objects.get(id=book_id)
            books.delete()
            return Response({"message": "Book deleted Successfully", "status": 200, "data": {}},
                            status=200)
        except Exception as e:
            logger.exception(e)
            return Response({"message": str(e), "status": 400, "data": {}}, status=400)
