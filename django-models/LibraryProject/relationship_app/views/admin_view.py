from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')