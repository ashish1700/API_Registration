
from django.contrib import admin
from django.urls import path, include
from app1 import views
# from video import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Ashish",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Ashish.local"),
      license=openapi.License(name="BSD License"),
   ),
   
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name = 'signup'),
    path('login/', views.loginpage, name = 'login'),
    # path('home/', views.homepage, name = 'home'),
    # path('video/', include("video.urls")),
    path('home/', include("video.urls")),
    path('api/v1/', include("endpoint.urls")),
    path('api/v2/',include("quiz.urls")),
    path('logout/', views.logoutpage, name = 'logout'),
   #  path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    
    