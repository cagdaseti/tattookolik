from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from . forms import ArticleForm
from . models import Article
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def articleDetail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    return render(request, "article-detail.html", {"article": article})


def articleDashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "article-dashboard.html", context)


def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale başarılı bir şekilde oluşturuldu...")
        return redirect("index")
    return render(request, "add-article.html", {"form": form})
