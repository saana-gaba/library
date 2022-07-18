from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book, RentBook, RentHistory

# Create your views here.

def home_page(request):
    return render(request, "books/home_page.html")

def all_books(request):
    all_books = list(Book.objects.all())
    all_rented_books = list(RentBook.objects.filter(user = request.user))

    for i in all_rented_books:
        for j in all_books:
            if (i.book.id == j.id):
                all_books.remove(j)

    return render(request, "books/all_books.html", {
        "books" : all_books,
    })

def rent_book(request, pk):
    if request.method == "POST":
        selected_book = Book.objects.get(id=pk)
        
        try:
            rented_or_not = RentBook.objects.get(book = selected_book, user = request.user)
        except:
            rented_or_not = None

        if not rented_or_not:
            rented_book = RentBook.objects.create(user = request.user, book = selected_book)
            rented_book.save()
            add_to_history = RentHistory.objects.create(book = selected_book, user = request.user, rent_type="REN")
            add_to_history.save()
            selected_book.stock += 1
            selected_book.save()



    return render(request, "books/book_rented.html", {
        "book" : selected_book
    })

def rent_history (request):
    history = RentHistory.objects.filter(user = request.user)

    return render(request, "books/rent_history.html", {
        "history" : history
    })

def rented_books(request):
    rented_book = RentBook.objects.filter(user = request.user)
    return render(request, "books/rented_books.html", {
        "books" : rented_book
    })

def return_book(request, pk):
    selected_remted_book = RentBook.objects.get(book=pk)
    if request.method == "POST":
        selected_remted_book.delete()

        selected_book = Book.objects.get(id=pk)
        selected_book.stock +=1
        selected_book.save()

        add_to_history = RentHistory.objects.create(book = selected_book, user = request.user, rent_type="RET")
        add_to_history.save()
        
        
    return render(request, "books/return_book.html", {
        "book" : selected_remted_book
    })
    