from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoryList.as_view(), name='categories_list'),
    path('posts/', views.PostList.as_view(), name='posts_list'),
    path('posts/<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/', views.AddComment.as_view(), name='add_comment'),
    path('comments/<int:id>/',
         views.CommentDetail.as_view(),
         name='comment_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
