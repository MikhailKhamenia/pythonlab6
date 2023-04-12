from django.contrib import admin
from django.urls import path, include

from laba.views import *

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customerchange/<int:pk>/',CustomerChange.as_view(), name='customer-change'),
    path('customers/<int:pk>/', CustomerAPIGet.as_view(), name='one-customer'),
    path('customers/new/', CustomerAPIList.as_view(), name='new-customer'),
]