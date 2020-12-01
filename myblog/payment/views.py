from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from payment.forms import FormModelStudent
from payment.models import ModelStudent
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.    

#createview
@method_decorator(login_required,name='dispatch')
class CreateModelView(CreateView):
    form_class = FormModelStudent
    template_name = 'payment/createmodel*.html'
    success_url = '/modelstudentlist/'



#updateview
@method_decorator(login_required,name='dispatch')
class UpdateModelView(UpdateView):
    model = ModelStudent
    form_class = FormModelStudent
    template_name = 'payment/createmodel*.html'
    success_url = '/modelstudentlist/'



#listview
@method_decorator(login_required,name='dispatch')
class ModelListView(ListView):
    model = ModelStudent
    template_name = 'payment/modellist*.html'
    ordering = ('id')

    # def get_queryset(self): #order by 'moh'
    #     return ModelPost.post.filter(name__icontains='moh')

# detail view for model
@method_decorator(login_required,name='dispatch')
class ModelDetailView(DetailView):
    model = ModelStudent
    template_name = 'payment/modeldetail*.html'

# delete view
@method_decorator(login_required,name='dispatch')
class DeleteModelView(DeleteView):
    model = ModelStudent
    template_name = 'payment/deletemodel.html'
    success_url = '/modelstudentlist/'

#list view
# @method_decorator(login_required,name='dispatch')
# class ModelListView(ListView):
#     template_name = 'payment/modellist*.html'
#     ordering = ('id')

#     def dispatch(self, request, *args, **kwargs):
#         models = kwargs.get('models', None)
#         if models == 'modelstudent':
#             self.model = ModelStudent
#         elif models == 'modelteacher':
#             self.model = ModelTeacher
#         return super(ModelListView, self).dispatch(request, *args, **kwargs)

#     def get_queryset(self):
        # return self.model.modelmanager.all()


#detail view
# @method_decorator(login_required,name='dispatch')
# class ModelDetailView(DetailView):
#     template_name = 'payment/modeldetail*.html'

#     def dispatch(self, request, *args, **kwargs):
#         models = kwargs.get('models', None)
#         if models == 'modelstudent':
#             self.model = ModelStudent
#         elif models == 'modelteacher':
#             self.model = ModelTeacher
#         return super(ModelDetailView, self).dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return self.model.modelmanager.all()



#delete view
# @method_decorator(login_required,name='dispatch')
# class DeleteModelView(DeleteView):
#     template_name = 'payment/deletemodel.html'
#     success_url = '/'

#     def dispatch(self, request, *args, **kwargs):
#         models = kwargs.get('models', None)
#         if models == 'modelstudent':
#             self.model = ModelStudent
#         elif models == 'modelteacher':
#             self.model = ModelTeacher
#         return super(DeleteModelView, self).dispatch(request, *args, **kwargs)

#     def get_queryset(self):
#         return self.model.modelmanager.all()

