import django_tables2 as tables
from django_tables2.utils import A
from catalog.models import Book


class BookTable(tables.Table):
#    title = tables.LinkColumn('book-detail', args=[A('pk')])
#    author = tables.LinkColumn('book-detail', args=[A('pk')])
    pass

    class Meta:
        model = Book
        fields = ['title','author', 'genre', 'isbn']
        attrs = {"id": "bk_table", "class": "table-striped table-bordered"}
        empty_text = 'there are no books '
