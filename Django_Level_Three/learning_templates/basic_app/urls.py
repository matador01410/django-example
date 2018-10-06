from django.urls import path
from . import views

# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    path('relatives/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]