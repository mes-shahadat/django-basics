from django.urls import path
from blogpost.views import ContactFormView, CreatePostView, UpdatePostView, PostListView, PostDetailView, DeletePostView
# from django.contrib.auth.decorators import login_required

urlpatterns = [
    # contact form urls
    path('contactform/',ContactFormView.as_view(),name='contactformurl'),

    # create, update, delete, list and detail post urls
    path('createpost/',CreatePostView.as_view(),name='createposturl'),
    path('updatepost/<int:pk>/',UpdatePostView.as_view(),name='updateposturl'),
    path('postlist/',PostListView.as_view(),name='postlisturl'),
    # path('postdetail/<int:pk>/',login_required(PostDetailView.as_view()),name='postdetailurl'),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name='postdetailurl'),
    path('deletepost/<int:pk>/',DeletePostView.as_view(),name='deleteposturl'),
]
