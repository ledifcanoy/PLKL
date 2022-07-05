from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.mainpage, name="mainpage"),   
    path('branch/',views.branch, name="branch"),
    path('show/',views.show, name="show"),
    path('information/',views.information, name="information"),
    path('table/',views.table, name="table"),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('cancel1/<int:id>', views.cancel1, name='cancel1'),
    path('cancel2/<int:id>', views.cancel2, name='cancel2'),
    path('update/<int:id>', views.update, name='update'),

]