from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm

# Create your views here.

def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    # context['images'] = images
    return render(request,"home/index.html",context)


def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all()
    return render(request, 'manage/carousel_list.html', context )


def carousel_update(request, pk):
    context = dict()
    context['item'] = Carousel.objects.get(pk=pk)
    return render(request, 'manage/carousel_update.html', context )


# stuff not checked
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    # item = Carousel.objects.first()
    # context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES.get('cover_image'))
        # create is deleted
        form = CarouselModelForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid:
            form.save()
        messages.success(request,'Resim eklendi...')
    return render(request,'manage/carousel_create.html',context)
