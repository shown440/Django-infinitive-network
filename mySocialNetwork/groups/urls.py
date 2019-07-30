# GROUPS URLS.PY

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('post/in/<slug:slug>', views.SingleGroup.as_view(), name='single'),

    # LEAVE AND JOIN VIEW --- URLS
    path('join/<slug:slug>', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>', views.LeaveGroup.as_view(), name='leave'),

]