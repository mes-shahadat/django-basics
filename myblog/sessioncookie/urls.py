from django.urls import path
from sessioncookie.views import sessioncookie, getsessioncookies, setsessioncookies, delsessioncookies, testsessioncookies

urlpatterns = [
    path('sessioncookie/',sessioncookie,name='sessioncookieurl'),
    path('getsessioncookies/',getsessioncookies,name='getsessioncookieurl'),
    path('setsessioncookie/',setsessioncookies,name='setsessioncookieurl'),
    path('delsessioncookie/',delsessioncookies,name='delsessioncookieurl'),
    path('testsessioncookie/',testsessioncookies,name='testsessioncookieurl'),
]