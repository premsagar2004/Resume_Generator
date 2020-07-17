from django.shortcuts import render


def home(request):
    return render(request, 'resume_data/preview1.html')
