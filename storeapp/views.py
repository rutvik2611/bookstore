from django.shortcuts import render
from rest_framework import viewsets

from storeapp import models, serializers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
        This to manage user 
        creation, list, update and delete
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
        This to manage books 
        creation, list, update and delete
    """
    queryset = models.Books.objects.all()
    serializer_class = serializers.BookSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """
        This to manage transaction 
        creation, list, update and delete
    """
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

class LibraryViewSet(viewsets.ModelViewSet):
    """
        This to manage library 
        creation, list, update and delete
    """
    queryset = models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer


class LibraryBooksView(APIView):

    """
        This to view the available books in library
        by library id with book data with rented book
    """

    def get(self, request, library_id, *args, **kwargs):
        try:
            library_books = models.Library.objects.get(id=library_id).books.all()
            library_data = []
            for book in library_books:
                d = models.Transaction.objects.filter(id=book.id).first()
                is_rented = False
                if d is not None:
                    is_rented = d.is_returned
                library_data.append({
                    'library': library_id,
                    'book_title': str(book.title),
                    'is_rented': is_rented
                })
            return Response(data=library_data)
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TransactionView(APIView):

    """
        This to view the books rented by user
        by userid with book data
    """

    def get(self, request, user_id, *args, **kwargs):
        try:
            books_by_user = []
            qs = models.Transaction.objects.select_related('rented_by', 'book').filter(rented_by=user_id)
            data = {}
            data['user'] = qs.first().rented_by.email
            for q in qs.iterator():
                books_by_user.append(
                    {
                        'id': q.book.id,
                        'title': q.book.title,
                        'isbn': q.book.isbn
                    }
                )
            
            data['books'] = books_by_user

            return Response(data=data)
        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)