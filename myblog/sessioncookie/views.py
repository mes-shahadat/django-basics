from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

# need to know django rest framework in order to use session in real example like in registration views
# in generic view you have to use get_context_data method to insert session
# if you need to send anything like object or context or session to template you need to use get_context_data method
#example:

# class ProductDetail(DetailView):
#     model = Producto
#     template_name = 'productos/product_detail.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(ProductDetail, self).get_context_data(**kwargs)
#         if not 'recent' in self.request.session or not self.request.session['recent']:
#             self.request.session['recent'] = [self.object.pk]
#         else:
#             recentList = self.request.session['recent']
#             recentList.append(self.object.pk)
#             self.request.session['recent'] = recentList
#         # Add in a QuerySet of featured products
#         context['product_list'] = Producto.objects.filter(featured=True).exclude(pk=self.object.pk)
#         context['recent_list'] = Producto.objects.filter(pk__in=recentList)
#         return context


def sessioncookie(request):
    return render(request,'sessioncookie/sessioncookie.html')


def getsessioncookies(request):
    if 'username' in request.session:
        username = request.session['username']# gets cookie but doesn't set default, expires means error
        cookie = request.session.get('cookie', default='empty')
        keys = request.session.keys()
        items = request.session.items() #item mean key and value both
        request.session.modified = True #gets modified after refresh
        print(f'session cookie age  (default 2 weeks): {request.session.get_session_cookie_age()}')
        print(f'session expiry age  (default 2 weeks): {request.session.get_expiry_age()}')
        print(f'session expiry date (default 2 weeks): {request.session.get_expiry_date()}')
        print(f'session expire at browser exit: {request.session.get_expire_at_browser_close()}')
        return render(request,'sessioncookie/getsessioncookies.html',{'cookie':cookie, 'username':username,'keys':keys,'items':items})
    else:
        messages.info(request,'your session has expired')
        return HttpResponseRedirect('/sessioncookie/')


def setsessioncookies(request):
    request.session['cookie']='mess'# cookie is key and mess is value
    request.session['username']='mohammad yasin'# username is key and mohammad yasin is value
    request.session.set_expiry(20)# 0 means expire at browser exit,you can also set expiry SESSION_COOKIE_AGE = 400 in setting
    messages.info(request,'session cookies setted successfully')
    return HttpResponseRedirect('/sessioncookie/')

def delsessioncookies(request):
    request.session.flush()
    request.session.clear_expired()
    messages.info(request,'all cookie has been deleted permanatly !')
    return HttpResponseRedirect('/sessioncookie/')

def testsessioncookies(request):
    print(f'test cookie inserted: True, ignore: {request.session.set_test_cookie()}')
    print(f'test cookie working:{request.session.test_cookie_worked()}')
    print(f'deleted test cookie: True, ignore: {request.session.delete_test_cookie()}')
    messages.info(request,'test session cookies setted successfully, check your console')
    return HttpResponseRedirect('/sessioncookie/')