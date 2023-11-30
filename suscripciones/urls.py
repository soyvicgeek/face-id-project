from django.urls import path
from . import views

urlpatterns = [
    path('', views.SuscripcionListView.as_view(), name='subs_list'),
    path('new/', views.SuscripcionCreateView.as_view(), name='sub_new'),
    path('update/<pk>/', views.SuscripcionUpdateView.as_view(), name='sub_update'),
    path('delete/<pk>/', views.SuscripcionDeleteView.as_view(), name='sub_delete')
]
