
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from registration.forms import FormLogin,FormPasswordChange,FormPasswordReset,FormSetPassoword, FormRegister,FormUserData,FormAdminData
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.

#user register view
class RegisterView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            form = FormRegister()
            return render(request,'registration/register.html',{'form':form})
        else:
            messages.info(request,'you are already registered in')
            return HttpResponseRedirect('/')
    def post(self,request):
        form = FormRegister(request.POST)
        if form.is_valid:
            user = form.save()
            group = Group.objects.get_or_create(name='manager')# get group if exists else creates group
            content_type = ContentType.objects.get(app_label='blogpost', model='modelpost')
            perms = Permission.objects.filter(content_type=content_type)
            group = Group.objects.get(name='manager')
            for p in perms:
                group.permissions.add(p)# add all model permission to group
            user.groups.add(group)# adds user(form.save) to group(group.object.get(name='manager'))
            messages.info(request,'you have been successfully registerd, and aded to manager group. plz login now')
            return HttpResponseRedirect('/userlogin/')


#user login logout view
class UserLoginView(SuccessMessageMixin,LoginView):
    redirect_authenticated_user = True
    template_name = 'registration/userlogin.html'
    authentication_form = FormLogin
    success_message = "logged in successfully"

@method_decorator(login_required,name='dispatch')
class UserLogoutView(LogoutView):
    template_name = 'registration/userlogout.html'
    success_url ='/'


#user password change view

@method_decorator(login_required,name='dispatch')
class ChangePassView(PasswordChangeView):
    form_class = FormPasswordChange
    template_name = 'registration/changepass.html'
    success_url = '/profile/'
    # success_url = '/changepassdone/'


class ChangePassDoneView(PasswordChangeDoneView):
    template_name = 'registration/changepassdone.html'


#password reset view

@method_decorator(login_required,name='dispatch')
class EmailFormView(PasswordResetView):
    form_class = FormPasswordReset
    template_name = 'registration/emailform.html'
    success_url = '/emailsent/'
    email_template_name = 'registration/email.html'

class EmailSentView(PasswordResetDoneView):
    template_name = 'registration/emailsent.html'

class ResetFormView(PasswordResetConfirmView):
    form_class = FormSetPassoword
    template_name = 'registration/resetform.html'
    success_url = '/resetcomplete/'

class ResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/resetcomplete.html'


#profile view

@method_decorator(login_required,name='dispatch')
class Profile(View):
    def get(self,request, id=None):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                if id==None:
                    form = FormAdminData(instance=request.user)
                else:
                    pi = User.objects.get(pk=id)
                    form = FormAdminData(instance=pi)
                users = User.objects.all()
            else:
                form = FormUserData(instance=request.user)
                users = None

            fullname = self.request.user.get_full_name()
            groups =  Group.objects.filter(user = self.request.user)
            return render(request,'registration/profile.html',{'form':form, 'user':self.request.user, 'users':users, 'groups':groups,'fullname':fullname})
        else:
            messages.info(request,'you need to login in order to see your profile')
            return HttpResponseRedirect('/userlogin/')
            
    def post(self,request,id=None):
            if request.user.is_superuser:
                if id==None:
                    form = FormAdminData(data=request.POST,instance=request.user)
                else:
                    pi = User.objects.get(pk=id)
                    form = FormAdminData(data=request.POST,instance=pi)
            else:
                form = FormUserData(data=request.POST,instance=request.user)

            if form.is_valid():
                messages.info(request,'saved successfully !')
                form.save()
            fullname = self.request.user.get_full_name()
            groups =  Group.objects.filter(user = self.request.user)
            return render(request,'registration/profile.html',{'form':form, 'user':self.request.user, 'groups':groups,'fullname':fullname})

