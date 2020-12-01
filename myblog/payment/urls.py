from django.urls import path
from payment.views import CreateModelView, UpdateModelView, DeleteModelView, ModelDetailView, ModelListView
from payment.forms import FormModelStudent, FormModelTeacher,FormModelContractor,FormModelCenter,FormModelCenterStudent, FormProxyModelCenterStudent
from payment.models import ModelStudent, ModelTeacher, ModelContractor, ModelCenter, ModelCenterStudent, ProxyModelCenterStudent
from django.contrib.auth.decorators import permission_required




urlpatterns = [
    # model student: create, update, delete, list and detail model urls 
    path('createmodelstudent/',permission_required('payment.add_modelstudent', raise_exception=True)(CreateModelView.as_view()),name='createmodelstudenturl'),

    path('updatemodelstudent/<int:pk>/',permission_required('payment.change_modelstudent', raise_exception=True)(UpdateModelView.as_view()),name='updatemodelstudenturl'),

    path('modelstudentlist/',ModelListView.as_view(),name='modelstudentlisturl'),

    path('modelstudentdetail/<int:pk>/',permission_required('payment.view_modelstudent', raise_exception=True)(ModelDetailView.as_view()),name='modelstudentdetailurl'),

    path('deletemodelstudent/<int:pk>/',permission_required('payment.delete_modelstudent', raise_exception=True)(DeleteModelView.as_view()),name='deletemodelstudenturl'),


    # model teacher: create, update, delete, list and detail model urls
    path('createmodelteacher/',permission_required('payment.add_modelteacher', raise_exception=True)(CreateModelView.as_view(form_class=FormModelTeacher,success_url = '/modelteacherlist/')),name='createmodelteacherurl'),

    path('updatemodelteacher/<int:pk>/',permission_required('payment.change_modelteacher', raise_exception=True)(UpdateModelView.as_view(form_class=FormModelTeacher,model=ModelTeacher,success_url = '/modelteacherlist/')),name='updatemodelteacherurl'),

    path('modelteacherlist/',(ModelListView.as_view(model=ModelTeacher)),name='modelteacherlisturl'),

    path('modelteacherdetail/<int:pk>/',permission_required('payment.view_modelteacher', raise_exception=True)(ModelDetailView.as_view(model=ModelTeacher)),name='modelteacherdetailurl'),

    path('deletemodelteacher/<int:pk>/',permission_required('payment.delete_modelteacher', raise_exception=True)(DeleteModelView.as_view(model=ModelTeacher,success_url = '/modelteacherlist/')),name='deletemodelteacherurl'),


    # model contractor: create, update, delete, list and detail model urls
    path('createmodelcontractor/',permission_required('payment.add_modelcontractor', raise_exception=True)(CreateModelView.as_view(form_class=FormModelContractor,success_url = '/modelcontractorlist/')),name='createmodelcontractorurl'),

    path('updatemodelcontractor/<int:pk>/',permission_required('payment.change_modelcontractor', raise_exception=True)(UpdateModelView.as_view(form_class=FormModelContractor,model=ModelContractor,success_url = '/modelcontractorlist/')),name='updatemodelcontractorurl'),

    path('modelcontractorlist/',(ModelListView.as_view(model=ModelContractor)),name='modelcontractorlisturl'),

    path('modelcontractordetail/<int:pk>/',permission_required('payment.view_modelcontractor', raise_exception=True)(ModelDetailView.as_view(model=ModelContractor)),name='modelcontractordetailurl'),

    path('deletemodelcontractor/<int:pk>/',permission_required('payment.delete_modelcontractor', raise_exception=True)(DeleteModelView.as_view(model=ModelContractor,success_url = '/modelcontractorlist/')),name='deletemodelcontractorurl'),


    # model center: create, update, delete, list and detail model urls
    path('createmodelcenter/',permission_required('payment.add_modelcenter', raise_exception=True)(CreateModelView.as_view(form_class=FormModelCenter,success_url = '/modelcenterlist/')),name='createmodelcenterurl'),

    path('updatemodelcenter/<int:pk>/',permission_required('payment.change_modelcenter', raise_exception=True)(UpdateModelView.as_view(form_class=FormModelCenter,model=ModelCenter,success_url = '/modelcenterlist/')),name='updatemodelcenterurl'),

    path('modelcenterlist/',(ModelListView.as_view(model=ModelCenter)),name='modelcenterlisturl'),

    path('modelcenterdetail/<int:pk>/',permission_required('payment.view_modelcenter', raise_exception=True)(ModelDetailView.as_view(model=ModelCenter)),name='modelcenterdetailurl'),

    path('deletemodelcenter/<int:pk>/',permission_required('payment.delete_modelcenter', raise_exception=True)(DeleteModelView.as_view(model=ModelCenter,success_url = '/modelcenterlist/')),name='deletemodelcenterurl'),


    # model center student: create, update, delete, list and detail model urls
    path('createmodelcenterstudent/',permission_required('payment.add_modelcenterstudent', raise_exception=True)(CreateModelView.as_view(form_class=FormModelCenterStudent,success_url = '/modelcenterstudentlist/')),name='createmodelcenterstudenturl'),

    path('updatemodelcenterstudent/<int:pk>/',permission_required('payment.change_modelcenterstudent', raise_exception=True)(UpdateModelView.as_view(form_class=FormModelCenterStudent,model=ModelCenterStudent,success_url = '/modelcenterstudentlist/')),name='updatemodelcenterstudenturl'),

    path('modelcenterstudentlist/',(ModelListView.as_view(model=ModelCenterStudent)),name='modelcenterstudentlisturl'),

    path('modelcenterstudentdetail/<int:pk>/',permission_required('payment.view_modelcenterstudent', raise_exception=True)(ModelDetailView.as_view(model=ModelCenterStudent)),name='modelcenterstudentdetailurl'),

    path('deletemodelcenterstudent/<int:pk>/',permission_required('payment.delete_modelcenterstudent', raise_exception=True)(DeleteModelView.as_view(model=ModelCenterStudent,success_url = '/modelcenterstudentlist/')),name='deletemodelcenterstudenturl'),


    # proxy model center student: create, update, delete, list and detail model urls
    path('createproxymodelcenterstudent/',permission_required('payment.add_proxymodelcenterstudent', raise_exception=True)(CreateModelView.as_view(form_class=FormProxyModelCenterStudent,success_url = '/proxymodelcenterstudentlist/')),name='createproxymodelcenterstudenturl'),

    path('updateproxymodelcenterstudent/<int:pk>/',permission_required('payment.change_proxymodelcenterstudent', raise_exception=True)(UpdateModelView.as_view(form_class=FormProxyModelCenterStudent,model=ProxyModelCenterStudent,success_url = '/proxymodelcenterstudentlist/')),name='updateproxymodelcenterstudenturl'),

    path('proxymodelcenterstudentlist/',(ModelListView.as_view(model=ProxyModelCenterStudent)),name='proxymodelcenterstudentlisturl'),

    path('proxymodelcenterstudentdetail/<int:pk>/',permission_required('payment.view_proxymodelcenterstudent', raise_exception=True)(ModelDetailView.as_view(model=ProxyModelCenterStudent)),name='proxymodelcenterstudentdetailurl'),

    path('deleteproxymodelcenterstudent/<int:pk>/',permission_required('payment.delete_proxymodelcenterstudent', raise_exception=True)(DeleteModelView.as_view(model=ProxyModelCenterStudent,success_url = '/proxymodelcenterstudentlist/')),name='deleteproxymodelcenterstudenturl'),
]
