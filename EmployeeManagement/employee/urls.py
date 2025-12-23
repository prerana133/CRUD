from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details/',views.employee_details,name='details'),
    path('add/',views.add_emp,name='add'),
    path('update/<int:id>/',views.update_emp,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
