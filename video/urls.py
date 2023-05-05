from django.urls import path, include
from video import views
# from rest_framework import routers
# router =  routers.SimpleRouter(trailing_slash=False)

# router = routers.DefaultRouter()
# router.register("api", views.APItestViewSet, basename = "api")


urlpatterns = [
    path("",views.index,name="home"),
    path('addvideo/', views.addvideoview, name='addvideo'),
    path('deletevideo/', views.deleteview, name='deletevideo')
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path("api/", views.APItestViewSet.as_view(), name='api')
]