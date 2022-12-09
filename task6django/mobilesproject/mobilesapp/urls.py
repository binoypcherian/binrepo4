from django.urls import path, include

from mobilesapp import views
app_name='mobileapp'

urlpatterns = [
    path('',views.list,name='list'),
    path('details/<int:mobile_id>/',views.detail,name='detail'),
    path('details/<int:mobile_id>/deleteexist/',views.delete,name='delete'),
    path('addnew/',views.add,name='add'),
    path('details/<int:mobile_id>/editexist/',views.edit,name='edit'),
]