from django.shortcuts import render


def home_page(request):
    context = {
        'title': 'Welcome to the home page'
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'Welcome to the about page'
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    context = {
        'title': 'Welcome to the contact page'
    }
    return render(request, 'contact/view.html', context)
