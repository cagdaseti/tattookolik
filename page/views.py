from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import slugify
from .models import Carousel,Page
from .forms import CarouselModelForm,PageModelForm
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# User
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published").exclude(cover_image='')
    # context['images'] = images
    return render(request,"home/index.html",context)


# Admin
# list
@staff_member_required
def page_list(request):
    context = dict()
    context['items'] = Page.objects.all().order_by("-pk")
    return render(request, 'manage/page_list.html', context )


@staff_member_required
def manage_list(request):
    context = dict()
    return render(request, 'manage/manage.html',context)


@staff_member_required
def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by("-pk")
    return render(request, 'manage/carousel_list.html', context )


# update
# stuff not checked
@staff_member_required
def carousel_update(request, pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk}  - Carousel Update Form"
    context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        form = CarouselModelForm(
            request.POST,
            request.FILES,
            instance=item,    
        )
        if form.is_valid:
            form.save()
            messages.success(request,'Güncelleme başarılı')
            return redirect('carousel_update',pk)
    return render(request, 'manage/form.html', context )


@staff_member_required
def page_update(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk}  - Page Update Form"
    context['form'] = PageModelForm(instance=item)
    if request.method == 'POST':
        form = PageModelForm(
            request.POST,
            request.FILES,
            instance=item,    
        )
        if form.is_valid:
            item = form.save(commit=False)
            if item.slug == '':
                item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,'Güncelleme başarılı')
            return redirect('page_update',pk)
    return render(request, 'manage/form.html', context )


# create
@staff_member_required
def carousel_create(request):
    context = dict()
    context['form'] = CarouselModelForm()
    context['title'] = "Carousel Create Form"
    # item = Carousel.objects.first()
    # context['form'] = CarouselModelForm(instance=item)
    if request.method == 'POST':
        # create is deleted
        form = CarouselModelForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid:
            form.save()
            return redirect('carousel_list')
            messages.success(request,'Resim eklendi...')
    return render(request,'manage/form.html',context)


@staff_member_required
def page_create(request):
    context = dict()
    context['title'] = "Page Create Form"
    context['form'] = PageModelForm()
    if request.method == 'POST':
        form = PageModelForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid:
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            return redirect('page_list')
            messages.success(request,'Resim eklendi...')
    return render(request,'manage/form.html',context)


@staff_member_required
def page_delete(request,pk):
    item = Page.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect('page_list')
