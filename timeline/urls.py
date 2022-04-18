from django.urls import path

from timeline import views

app_name = 'timeline'
urlpatterns = [
    path('', views.index),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('like-post/<int:post_id>/', views.like_post, name='like_post'),
    path('comment-add/<int:post_id>', views.comment_add, name="comment_add")
]
