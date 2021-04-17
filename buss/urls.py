from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('form/', views.form, name="form"),
	path('payment/', views.payment, name="payment"),
	path('messages/', views.messages, name="messages"),
	path('download/', views.download, name="download"),
	path('rate/', views.rate, name="rate"),
	path('contact/', views.contact, name="contact"),
]