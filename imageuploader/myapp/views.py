from django.shortcuts import render
from .forms import ImageForm
from .models import Image
from django.shortcuts import render, HttpResponse

# Create your views here.
def home( request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("image uploaded successfully")
    form = ImageForm()
    img = Image.objects.all()

    return render(request, 'home.html', {'img':img,'form':form})