from django.views import View
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import render

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context
    

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  # ✅ <-- Add this
from django.urls import reverse_lazy
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context

class RegisterView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Optional: logs user in after registering
        return redirect(self.success_url)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ auto-login after registration
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


class LibraryDetailView(View):
    ...


from django.shortcuts import render
from django.views import View

def list_books(request):
    return render(request, "books.html")

class LibraryDetailView(View):
    pass


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_member(user):
    return user.groups.filter(name='Member').exists()

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

def is_admin(user):
    return user.is_superuser  # or use a group if you prefer


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

