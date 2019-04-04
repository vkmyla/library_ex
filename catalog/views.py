from django.shortcuts import render
from django_tables2 import RequestConfig

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from catalog.tables import BookTable

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic


class BookListView(generic.ListView):
    model = Book

#    template_name = 'django_tables2/bootstrap.html'  # Specify your own template name/locati
    def all_books(self):
        return Book.objects.all()

    def book_table_data(self):
        table = BookTable(Book.objects.all())
        RequestConfig(self.request).configure(table);
        #  RequestConfig(self.request, paginate={'per_page': 3}).configure(table);
        return table
#    context_object_name = 's_book_list'   # your own name for the list as a template variable
#    queryset = Book.objects.filter(title__icontains='Kundalini') # Get 5 books containing the title war
#    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/locati
#
#class BookDetailView(generic.DetailView):
#    model = Book
