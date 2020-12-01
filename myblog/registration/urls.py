from django.urls import path
from registration.views import UserLoginView,UserLogoutView,ChangePassView,ChangePassDoneView,EmailFormView,EmailSentView,ResetFormView,ResetCompleteView,RegisterView,Profile
from django.views.generic.base import TemplateView, RedirectView

urlpatterns = [

    # user registration and login, logout urls
    path ('register/',RegisterView.as_view(),name='registerurl'),
    path ('userlogin/',UserLoginView.as_view(),name='userloginurl'),
    path ('userlogout/',UserLogoutView.as_view(),name='userlogouturl'),

    # password change urls
    path ('changepass/',ChangePassView.as_view(),name='changepassurl'),
    path('changepassdone/',ChangePassDoneView.as_view(),name='changepassdoneurl'),

    # password reset urls
    path('emailform/',EmailFormView.as_view(),name='emailformurl'),
    path('emailsent/',EmailSentView.as_view(),name='emailsenturl'),
    path('resetform/<uidb64>/<token>/',ResetFormView.as_view(),name='resetformurl'),
    path('resetcomplete/',ResetCompleteView.as_view(),name='resetcompleteurl'),

    # profile urls
    path('profile/',Profile.as_view(),name='profileurl'),
    path('profile/<int:id>/',Profile.as_view(),name='profileinturl'),
]
