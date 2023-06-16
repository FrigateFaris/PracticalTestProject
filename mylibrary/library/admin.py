from django.contrib import admin
from library.models import Reader, BookRent, newBook

# Register your models here.
admin.site.register(newBook)
admin.site.register(Reader)
admin.site.register(BookRent)
