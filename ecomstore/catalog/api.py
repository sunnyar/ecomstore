from tastypie.resources import ModelResource
from tastypie.constants import ALL
from .models import Category

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        filtering = { "name" : ALL }