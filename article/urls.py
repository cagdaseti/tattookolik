from django.urls import path
from .views import (
    articleDashboard,
    articleCreate,
    articleDetail,
    articleList,
)

app_name = "article"

urlpatterns = [
    path('article/dashboard/', articleDashboard,name="articleDashboard"),
    path('article/add/', articleCreate,name="articleCreate"),
    path('article/detail/<int:pk>', articleDetail,name="articleDetail"),
    # path('article/update/<int:pk>', articleUpdate,name="articleUpdate"),
    # path('article/delete/<int:pk>', articleDelete,name="articleDelete"),
    path('article/list/', articleList,name="articleList"),
]
