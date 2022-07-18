from django.contrib import admin
from .models import Book, RentBook, RentHistory

# Register your models here.
admin.site.register(Book)
admin.site.register(RentBook)
admin.site.register(RentHistory)