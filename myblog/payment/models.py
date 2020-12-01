from django.db import models

#custom model manager
# class custommanager(models.Manager):
#      def get_queryset(self):
#         return super().get_queryset().order_by('name')

# Create your models here.

#abstract model
class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True


class ModelStudent(CommonInfo):
    fees = models.IntegerField()
    date = None
    modelmanager = models.Manager()

class ModelTeacher(CommonInfo):
    salary = models.IntegerField()
    modelmanager = models.Manager()

class ModelContractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()
    modelmanager = models.Manager()


#multilabel inheritance
class ModelCenter(models.Model):
    center_name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    modelmanager = models.Manager()

class ModelCenterStudent(ModelCenter):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    modelmanager = models.Manager()

#proxy model
class ProxyModelCenterStudent(ModelCenterStudent):
    # modelmanager = custommanager
    modelmanager = models.Manager()
    class Meta:
        proxy = True
        ordering = ['city']