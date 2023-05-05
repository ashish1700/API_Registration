from django.contrib import admin
from django.urls import path ,include
from endpoint.views import APItestViewSet, UserRegistrationView, UserLoginView
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'test', APItestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("get-details",UserDetailAPI.as_view()),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    
]