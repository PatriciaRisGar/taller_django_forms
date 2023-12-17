from django.forms import formset_factory
from django.shortcuts import redirect, render

# Create your views here.
from django.views import View

from books.models import Book
from books.forms import BookForm


class ListBookView(View):
    def get(self, request):
        return render(request, 'list_book.html', context={'books': Book.objects.all().order_by('-created_at')})

class CreateBookView(View):
    def get(self, request):
        return render(request, 'create_book.html', context={'form': formset_factory(BookForm,extra=2)})
    

    def post(self, request):
        formset = formset_factory(BookForm)(data=request.POST)
        if formset.is_valid():
            for form in formset:
                if form.haschanged():
                    form.save()
                    
            return redirect('list-book')
        else:
            return render(request, 'create_book.html', context={'form': formset})
