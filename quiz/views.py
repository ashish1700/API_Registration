from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from quiz.models import Questions , Videoo ,Testing_image , VideoFestival
from quiz.serilaizers import Questionserializer , Videooserializer , TestingImageSerializer , VideoFestivalSerializer
from rest_framework.views import APIView
from rest_framework import parsers
from rest_framework import status
from quiz import models
from rest_framework import filters
import django_filters.rest_framework
# from .response_messages import videoo_response

# Create your views here.

class VideoFestivalViewSet(viewsets.ModelViewSet):
    queryset = VideoFestival.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    serializer_class = VideoFestivalSerializer

    def create(self, request, *args, **kwargs):
        existing_data = VideoFestival.objects.all()

        if existing_data:
            existing_data.delete()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class VideooViewSet(viewsets.ModelViewSet):
    queryset = models.Videoo.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']
    serializer_class = Videooserializer
    model = models.Videoo


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        delete_response = {"status": "success", "message": "videoo deleted"}
        return JsonResponse(delete_response)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        update_response = {"status": "success", "message": "videoo updated"}
        return JsonResponse(update_response)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        create_response = {"status": "success", "message": "videoo created"}
        return JsonResponse(create_response)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    serializer_class = Questionserializer
    filterset_fields = ['question']
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['question']
    
    # def get(self, request, format=None):
    #     # Retrieve a single question
    #     question = Questions.objects.get(id=request.query_params.get('id'))
    #     serializer = Questionserializer(question)
    #     return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
         # Award 1 point for correct answer
        instance = serializer.instance
        if instance.answer == request.data.get('answer'):
            instance.score = 1
            instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update score if the answer is changed and correct
        if 'answer' in request.data and instance.answer == request.data.get('answer'):
            instance.score = 1
            instance.save()

        return Response(serializer.data)
    
    
    
class TestingImageViewSet(viewsets.ModelViewSet):
    queryset = Testing_image.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    serializer_class = TestingImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deletes_in_ten_seconds
        self.perform_destroy(instance)
        return Response(status=204)


