from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from blogpost.forms import FormContact, FormModelPost
from blogpost.models import ModelPost
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.models import Group

# Create your views here.

#formview
class ContactFormView(FormView):
    template_name = 'blogpost/contactform.html'
    form_class = FormContact
    success_url = '/userlogin/'
    # initial = {'name':'mess'} #default field name

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactFormView, self).form_valid(form)

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data.sender_name)

        # def form_valid(self,form):
        # print (form.cleaned_data['name'])
        # print (form.cleaned_data['email'])
        # print (form.cleaned_data['password'])
        # return HttpResponse('form sent was successfull')
    

#createview
@method_decorator(login_required,name='dispatch')
@method_decorator(permission_required('blogpost.add_modelpost', raise_exception=True),name='dispatch')
class CreatePostView(CreateView):
    form_class = FormModelPost
    template_name = 'blogpost/createpost*.html'
    success_url = '/'

    def form_valid(self, form):# make the user in a model default to the current user 
            self.object = form.save(commit=False)
            self.object.createdby = self.request.user
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())

#updateview

@method_decorator(login_required,name='dispatch')
@method_decorator(permission_required('blogpost.change_modelpost', raise_exception=True),name='dispatch')
class UpdatePostView(UpdateView):
    model = ModelPost
    form_class = FormModelPost
    template_name = 'blogpost/createpost*.html'
    success_url = '/postlist/'


#listview
@method_decorator(login_required,name='dispatch')
class PostListView(ListView):
    model = ModelPost
    # template_name_suffix = '_mess'
    # context_object_name = 'messobjects'
    template_name = 'blogpost/postlist.html'
    ordering = ('id')
    paginate_by = 3
    paginate_orphans = 1
    
    # def get_queryset(self): #order by 'moh'
    #     return ModelPost.modelmanager.filter(name__icontains='moh')
  
    def get_context_data(self,*args,**kwargs):#to get to 1st page if wrong page number or other str inputed
        try:
            return super(PostListView,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView,self).get_context_data(*args,**kwargs)
        
#detail view for mess model
@method_decorator(login_required,name='dispatch')
class PostDetailView(DetailView):
    model = ModelPost
    template_name = 'blogpost/postdetail.html'
    # pk_url_kwarg = 'mess'
    
    
    # def get_context_data(self,*args,**kwargs):# send as many model object you want by overriding this method
    #     context = super().get_context_data(*args,**kwargs)
    #     context ['groups'] =  Group.objects.filter(user = self.request.user)
    #     # context ['newob'] = mess.objects.all()# use for loop in newob to get this models fields data
    #     return context


#delete view

@method_decorator(login_required,name='dispatch')
@method_decorator(permission_required('blogpost.delete_modelpost', raise_exception=True),name='dispatch')
class DeletePostView(DeleteView):
    model = ModelPost
    template_name = 'blogpost/deletepost.html'
    success_url = '/postlist/'

