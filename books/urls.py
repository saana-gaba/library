from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="index" ),
    path("all-books", views.all_books, name="all-books"),
    path("rent-history", views.rent_history, name="rent-history"),
    path("rented-books", views.rented_books, name="rented-books"),
    path("all-books/rent/<int:pk>", views.rent_book, name="rent-a-book"),
    path("all-books/return/<int:pk>", views.return_book, name="return-book"),
]