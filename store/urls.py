from django.urls import path
from django.conf.urls import url

from store import views

#app_name = 'store'

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name='store'),
	path('cart/', views.cart, name='cart'),
	path('checkout/', views.checkout, name='checkout'),
    path('test/', views.test, name='test'),

]
