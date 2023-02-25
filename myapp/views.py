from django.shortcuts import render
from django.views.generic import View
from .forms import ImageForm
from .models import Image
# Create your views here.

class home(View):
    def get(self, request):
        form = ImageForm()
        img = Image.objects.all()
        return render (request, 'myapp/home.html', {'form':form, 'img':img})

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            form = ImageForm()
        img = Image.objects.all()
        return render (request, 'myapp/home.html', {'form':form, 'img':img})