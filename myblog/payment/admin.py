from django.contrib import admin
from payment.models import ModelStudent, ModelTeacher, ModelContractor, ModelCenter, ModelCenterStudent,ProxyModelCenterStudent

# Register your models here.
@admin.register(ModelStudent)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','name','age','fees']

@admin.register(ModelTeacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ['id','name','age','date','salary']

@admin.register(ModelContractor)
class AdminContractor(admin.ModelAdmin):
    list_display = ['id','name','age','date','payment']

@admin.register(ModelCenter)
class AdminCenter(admin.ModelAdmin):
    list_display = ['id', 'center_name','city']

@admin.register(ModelCenterStudent)
class AdminCenterStudent(admin.ModelAdmin):
    list_display = ['id', 'center_name','city','name','roll']

@admin.register(ProxyModelCenterStudent)
class AdminModelProxyExamCenter(admin.ModelAdmin):
    list_display = ['id', 'center_name', 'city','name','roll']