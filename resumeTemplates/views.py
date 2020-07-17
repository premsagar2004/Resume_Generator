from django.shortcuts import render


def templates(request):
    return render(request, 'resumeTemplates/templates.html')

