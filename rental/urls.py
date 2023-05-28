from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:rental_id>/lend/', views.lend_book, name='lend-book'),
    path('books/<int:rental_id>/return/', views.return_book, name='return-book'),
    # دیگر لینک‌ها
]
