from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views import View
from django.shortcuts import render

#class based view

#@method_decorator(cache_page(30),name='dispatch')#need to use extra method_decorator to use other decorator
#class ThankyouView(View):
#    def get(self,request,id):
#       return render(request,'main/thankyou.html',{'id':id})
# path('thankyou/<int:id>',ThankyouView.as_view(),name='thankyouurl'),


#function based view

# @cache_page(60) #cache dacorator
# def thankyou(request,id):
#     return render(request,'main/thankyou.html',{'id':id})
# path('thankyou/<int:id>',thankyou,name='thankyouurl'),


#template based view

class navigateView(TemplateView):
    template_name = 'global/navigate.html'


#per view based caching
@method_decorator(cache_page(30),name='dispatch')#cache will update after every 30 seconds
class HomeView(TemplateView):
    template_name = 'main/home.html'

#per url based caching
class ContactView(TemplateView):
    template_name = 'main/contact.html'

#per template based caching
class AboutView(TemplateView):
    template_name = 'main/about.html'


#clear all caches
class ClearcacheView(View):
    def get(self,request):
        cache.clear()
        return render(request,'main/clearcache.html')

#low cache api

# def home(request):
#     cache_data = cache.get('movie','cache_expired')
#     if cache_data == 'cache_expired':
#         cache.set('movie', 'kimetsu no yaiba', 30)
#         cache_data = cache.get('movie')
#     return render(request,'main/home1.html',{'cache_data':cache_data})

# def home(request):
#     cache_data = cache.get_or_set('movie','kono_subarashi_in_kimson_world',30)
#     return render(request,'main/home1.html',{'cache_data':cache_data})

# def home(request):
#     movie = {'kono_name':'kono subarashi in crimsons world','kimetsu_name':'kimetsu no yaiba movie'}
#     cache.set_many(movie,30)
#     cache_data2 = cache.get_many(movie)
#     return render(request,'main/home1.html',{'cache_data2':cache_data2})

# def home(request):
#     cache.delete('kono_name')
#     return render(request,'main/home1.html')

# after setting roll cache
# def home(request):
#     dv = cache.decr('roll', delta=2)#decrease data by 2
#     print(dv)
#     return render(request,'main/home1.html')

# def home(request):
#     dv = cache.incr('roll', delta=2)#increase data by2
#     print(dv)
#     return render(request,'main/home1.html')

# def home(request):
#     cache.clear()#clears all caches
#     return render(request,'main/home1.html')

# path('',home1,name='home1url'),