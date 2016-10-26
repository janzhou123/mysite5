from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from books.models import Book
from forms import ContactForm
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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            # cd['subject'],
            # cd['message'],
            # cd.get('email', 'noreply@example.com'),
            # ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('books/contact_form.html', {'form': form})