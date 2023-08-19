from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('about/', views.about, name='blogs-about'),
    path('blog/<int:pk>/',views.blog_details,name='blogs-details'),
    path('blog_send_mail/',views.blog_send_mail,name='blog-send-mail'),
    path('blog/shared_mail/',views.sharedMail,name='shared-mail'),
    path('blog/comment/<int:pk>/', views.blog_comments, name='blog_comments'),
    path("blog/like/<int:pk>/",views.BlogPostLike,name='comment-like'),
    # path("blog/all-comments/",views.ALLComments,name='all-comment'),
]