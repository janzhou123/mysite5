from django.shortcuts import render_to_response,HttpResponse
from books.models import Book
# Create your views here.
def search_form(request):
    return render_to_response('books/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('books/search_results.html',
    {'books': books, 'query': q})
    else:
        return render_to_response('books/search_form.html', {'error': True})