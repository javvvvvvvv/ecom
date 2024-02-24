
from django.urls import path

from ecommerceapp import views
app_name='ecommerceapp'
urlpatterns = [

    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodet,name='prodcatdetail'),
   # path('<slug:product_slug>/',views.addtocart,name='prodcartdetail'),
]