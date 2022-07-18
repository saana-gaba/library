from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.book_title

class RentBook(models.Model):
    rent_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.book_title + self.user.first_name

class RentHistory(models.Model):
    RENT = "REN"
    RETURN = "RET"
    RENT_TYPE = [
        ("RET", "Return"),
        ("REN", "Rent")
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(auto_now_add=True)
    rent_type = models.CharField(max_length=3, choices=RENT_TYPE, default=RENT)

