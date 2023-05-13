from django.urls import path
from . import views
app_name= 'shopapp'

urlpatterns =[
    path('',views.allproduct,name="allproduct"),
    path('<slug:c_slug>/',views.allproduct,name="pro by cat"),
    path('<slug:c_slug>/<slug:product_slug>/',views.productde,name="product")
]