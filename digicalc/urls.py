from django.urls import path
from .import views
from .views import calculator_view

urlpatterns = [
		path('', views.digicalc, name='digicalc'),
		path('calculator/', calculator_view, name='calculator'),
]
