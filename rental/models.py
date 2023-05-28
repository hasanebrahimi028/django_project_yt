from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # سایر فیلدهای مرتبط

    def __str__(self):
        return self.title

class LibraryMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # سایر فیلدهای مرتبط
    class Meta:
        app_label = 'book_rental'

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(LibraryMember, on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField()
    is_lent = models.BooleanField(default=False)
    class Meta:
        app_label = 'book_rental'

    def __str__(self):
        return f"Rental #{self.id}"
