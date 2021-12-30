from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(), name='home'),
    path('post/new/',views.NewPostView.as_view(), name='post_new'),
    path('post/detail/<int:pk>',views.PostdetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>',views.PostEditView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post_delete'),
]