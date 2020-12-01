from django.urls import path
from main.views import HomeView, ContactView, AboutView, navigateView, ClearcacheView
from django.views.generic.base import RedirectView
from django.views.decorators.cache import cache_page

urlpatterns = [
    
    # ================================ home, contact, about urls ===========================================
    path('',HomeView.as_view(),name='homeurl'),
    path('contact/',ContactView.as_view(),name='contacturl'),
    path('contactcache/',cache_page(30) (ContactView.as_view()),name='contactcacheurl'),
    #cache will update after every 30 seconds
    path('about/',AboutView.as_view(),name='abouturl'),
    path('clearcache/',ClearcacheView.as_view(),name='clearcacheurl'),
    path('debug/',navigateView.as_view(),name='debugurl'),

    # ====================================== redirect urls =================================================
    path('home/',RedirectView.as_view(url='/'),name='homeurl'),
    path('index/',RedirectView.as_view(pattern_name='homeurl'),name='indexurl'),
    #if dynameic url has value and if nameurl is used instead of redirecting to a url then the nameurl will get the dynamic value also
    path('google/',RedirectView.as_view(url='https://www.google.com'),name='googleurl'),
]