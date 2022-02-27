from django.shortcuts import redirect, render, get_object_or_404,reverse
from .forms import ArticleModelForm
from .models import Article,Comment
from django.contrib import messages




def articleDetail(request, pk):
    # article = Article.objects.filter(pk=pk).first()
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    return render(request, "article/article-detail.html", {"article": article,"comments":comments})


def articleDashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "article/article-dashboard.html", context)


def articleCreate(request):
    context = dict()
    context['form'] = ArticleModelForm()
    context['title'] = "Article Create Form"
    if request.method == 'POST':
        form = ArticleModelForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid:
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Makale başarılı bir şekilde oluşturuldu...")
            return redirect('article:articleList')
    return render(request,'article/add-article.html',context)


def addComment(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(
            comment_author=comment_author,
            comment_content=comment_content
            )
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"pk":pk})) # ! detail olmayacak




def articleList(request):
    context = dict()
    context['article'] = Article.objects.all().order_by("-pk")
    return render(request, 'article/article-list.html', context )

