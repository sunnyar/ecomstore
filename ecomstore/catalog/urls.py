from django.conf.urls.defaults import patterns, include, url
from api import CategoryResource

category_resource = CategoryResource()

urlpatterns = patterns('ecomstore.catalog.views',
    url(r'^api/', include(category_resource.urls)),
    (r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),
    (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', {
        'template_name':'catalog/category.html'},'catalog_category'),
    (r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', {
        'template_name':'catalog/product.html'},'catalog_product'),
)