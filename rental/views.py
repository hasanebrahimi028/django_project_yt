from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Rental, Book
from django.core.paginator import Paginator

def lend_book(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    rental.is_lent = True
    rental.save()
    return redirect('book-list')

def return_book(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    rental.is_lent = False
    rental.save()
    return redirect('book-list')

def book_list(request):
    books = Book.objects.order_by('id')
    paginator = Paginator(books, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': page_obj.object_list,
        'page_obj': page_obj,
    }
    print(len(books))
    return render(request, "rental/book_list.html", {'books': books})
