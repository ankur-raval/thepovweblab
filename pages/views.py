from django.shortcuts import render, redirect


def index_view(request):
    return render(request, 'index.html')


def services_view(request):
    return render(request, 'services.html')


def contact_view(request):
    return render(request, 'contact.html')