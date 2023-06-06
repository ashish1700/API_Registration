from django.contrib import admin
from django.urls import path ,include
from endpoint.views import APItestViewSet, UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'test', APItestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("get-details",UserDetailAPI.as_view()),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('sendresetpasswordemail/', SendPasswordResetEmailView.as_view(), name='sendresetpasswordemail'),
    path('resetpassword/<uid>/<token>/',UserPasswordResetView.as_view(), name='resetpassword'),
    
]