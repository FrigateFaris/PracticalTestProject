from django.db import models


class newBook(models.Model):
    title = models.CharField(max_length=50, null=True)
    author_name = models.CharField(max_length=40, null=True)
    author_surname = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)
    publication_year = models.IntegerField(null=True)
    page_count = models.IntegerField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title} - {self.author_name} - {self.author_surname} - {self.genre} - {self.publication_year} - ' \
               f'{self.page_count} -{self.description}'


class Reader(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age} - {self.address}"


class BookRent(models.Model):
    book_title = models.CharField(max_length=50, null=True)
    reader_surname = models.CharField(max_length=20, null=True)
    rent_date = models.DateField(null=True)
    return_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.book_title} was rent to {self.reader_surname}: {self.rent_date} - {self.return_date}"

