from django.http import JsonResponse
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from . models import JsonData
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from .forms import FileForm




@login_required
def home(request):
    obj = JsonData.objects.get(user=request.user)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return render(request, 'resume_data/selectionPage.html')

    form = FileForm(instance=obj)
    return render(request, 'resume_data/home.html', {'form': form})


def load_json_table_format(request):
    obj = JsonData.objects.get(user=request.user)
    data = "media\\" + str(obj.file)
    data = Path(data)

    with open(data) as data:
        data = json.load(data)

    return render(request, 'resume_data/preview1.html', {'data': data})


from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from . utils import render_to_pdf
from pathlib import Path


class GeneratePdf1(View):

    def get(self, request, *args, **kwargs):
        obj = JsonData.objects.get(user=request.user)
        data = "media\\"+str(obj.file)
        data = Path(data)

        with open(data) as data:
            data = json.load(data)


        template = get_template('resume_data/temp1.html')
        context = {'data': data}
        html = template.render(context)
        pdf = render_to_pdf('resume_data/temp1.html',context)
        return HttpResponse(pdf, content_type='application/pdf')



def preview2(request):
    obj = JsonData.objects.get(user=request.user)
    data = "media\\" + str(obj.file)
    data = Path(data)

    with open(data) as data:
        data = json.load(data)
    return render(request, 'resume_data/preview2.html', {'data':data})


class GeneratePdf2(View):
    def get(self, request, *args, **kwargs):
        obj = JsonData.objects.get(user=request.user)
        data = "media\\"+str(obj.file)
        data = Path(data)

        with open(data) as data:
            data = json.load(data)

            template = get_template('resume_data/temp2.html')
            context = {'data': data}
            html = template.render(context)
            pdf = render_to_pdf('resume_data/temp2.html', context)
            return HttpResponse(pdf, content_type='application/pdf')





def preview3(request):
    return render(request, 'resume_data/preview3.html')