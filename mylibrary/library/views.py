from django.shortcuts import render
from library.models import newBook, Reader, BookRent


# Create your views here.
def show_start_page(request):
    return render(request, "index.html")


def show_showbooks_page(request):
    context = {"books": newBook.objects.all()}

    return render(request, "showBooks.html", context=context)


def show_showreader_page(request):
    context = {'readers': Reader.objects.all()}

    return render(request, 'showReader.html', context=context)


def show_showrent_page(request):
    context = {'rents': BookRent.objects.all()}

    return render(request, 'showRent.html', context=context)


def show_addbook_page(request):
    if request.method == "POST":
        book_title = request.POST.get("book_title")
        author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("book_author_surname")
        genre = request.POST.get("book_genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count")
        description = request.POST.get("description")

        newBook.objects.create(title=book_title,
                               author_name=author_name,
                               author_surname=author_surname,
                               genre=genre,
                               publication_year=publication_year,
                               page_count=page_count,
                               description=description)

    return render(request, "addBook.html")


def show_addreader_page(request):
    if request.method == "POST":
        name = request.POST.get("reader_name")
        surname = request.POST.get("reader_surname")
        age = request.POST.get("reader_age")
        address = request.POST.get("reader_address")

        Reader.objects.create(name=name,
                              surname=surname,
                              age=age,
                              address=address)

    return render(request, "addReader.html")


def show_addrent_page(request):
    if request.method == "POST":
        title = request.POST.get("book_title")
        reader = request.POST.get("reader_surname")
        rent_date = request.POST.get("rent_date")
        return_date = request.POST.get("return_data")

        BookRent.objects.create(book_title=title,
                                reader_surname=reader,
                                rent_date=rent_date,
                                return_date=return_date)

    return render(request, "addRent.html")


def show_deletebook_page(request):
    if request.method == 'POST':
        title = request.POST.get('book_title')
        del_book = newBook.objects.filter(title=title)
        del_book.delete()

    return render(request, 'deleteBook.html')


def show_deletereader_page(request):
    if request.method == 'POST':
        name = request.POST.get('reader_name')
        surname = request.POST.get('reader_surname')
        del_reader_datas = Reader.objects.get(name=name, surname=surname)
        del_reader_datas.delete()

    return render(request, 'deleteReader.html')


def show_deleterent_page(request):
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        reader_surname = request.POST.get('reader_surname')
        del_rent_datas = BookRent.objects.get(book_title=book_title, reader_surname=reader_surname)
        del_rent_datas.delete()

    return render(request, 'deleteRent.html')
