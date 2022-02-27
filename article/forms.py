from django import forms
from . models import Article,Comment


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_author", "comment_content"]