from django.contrib import admin
from django.urls import path ,include
from quiz.views import QuestionViewSet , VideooViewSet, TestingImageViewSet , VideoFestivalViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'quiz', QuestionViewSet)
router.register(r'videoos', VideooViewSet)
router.register(r'testing-images', TestingImageViewSet)
router.register(r'VideoFestival', VideoFestivalViewSet)


urlpatterns = [ 
    # path('quiz/', QuestionViewSet.as_view(), name='quiz'),
    path('', include(router.urls)),
    # path('videoo/', VideooViewSet.as_view(), name='videoo'),
]