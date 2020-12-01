from django.contrib import admin
from blogpost.models import ModelPost

# Register your models here.

@admin.register(ModelPost)
class AdminModelPost(admin.ModelAdmin):
    list_display = ('id','createdby','title','desc','publish_date','updated_at')

    # make the one to many field user in a model default to the current user 
    def get_changeform_initial_data(self, request): 
        get_data = super(AdminModelPost, self).get_changeform_initial_data(request)
        get_data['createdby'] = request.user.pk
        return get_data
