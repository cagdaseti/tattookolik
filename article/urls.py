from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('article-dashboard/', views.articleDashboard,name="article-dashboard"),
    path('add-article/', views.addArticle,name="add-article"),
    path('article-detail/<int:id>', views.articleDetail,name="article-detail"),
]
