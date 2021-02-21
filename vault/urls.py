from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create<slug:member_count>', views.create, name='create'),
    path('join', views.join, name='join'),
    path('create/success<slug:group_id>', views.create_success, name='create-success'),
    path('create/count', views.create_count, name='create-count'),
    path('join/failed', views.join_failed, name='join-failed')
]
