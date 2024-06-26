from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('test/', views.test_css, name='test_css'),
    path('test_pagina1/', views.test_pagina, name='test_pagina1'),
    path('final_test/', views.final_test, name='final_test'),
    path('final_eye/', views.final_eye, name='final_eye'),
    path('form/', views.get_form, name='form'),
    path('api/save-form/', views.save_form , name='api/save-form'),
    path('hey/', views.hey_txt , name='hey'),
    
]