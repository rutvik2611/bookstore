from django.urls import path
from storeapp import views


urlpatterns = [
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', views.UserViewSet.as_view({'delete': 'destroy', 'get' : 'retrieve', 'put': 'update'})),
    
    path('books/', views.BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('books/<int:pk>/', views.BookViewSet.as_view({'delete': 'destroy', 'get' : 'retrieve', 'put': 'update'})),

    path('transactions/', views.TransactionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('transactions/<int:pk>/', views.TransactionViewSet.as_view({'delete': 'destroy', 'get' : 'retrieve', 'put': 'update'})),
]
