from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('feedback/form', views.feedback_form_view, name='feedback_list'),
    path('feedback/list/', views.feedback_list_view, name='feedback_form'),
    path('contact/queries/', views.contact_queries_list_view, name='contact_queries_list')
]
