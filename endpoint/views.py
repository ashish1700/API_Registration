from django.shortcuts import render
from rest_framework import viewsets
from endpoint.models import APItest
from endpoint.serializers import APItestSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework import parsers
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.


class APItestViewSet(viewsets.ModelViewSet):
    queryset = APItest.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    serializer_class = APItestSerializer
  

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user= serializer.save()
            return Response({'msg': 'Registration Success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('Password')
            user = authenticate(email=email,password=password)
            if user is not None:
                return Response({'msg': 'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
    
  
  
  
  
  
  
  
  
  
  
  
  
    
# class NewUserAPI(APIView):
#     def get(self,request,*args,**kwargs):
#         user = Register.objects.get(id=request.user.id)
#         serializer = NewUserSerializer(user)
#         return Response(serializer.data)        
        
    
    
    
    


# class LoginViewSet(viewsets.ModelViewSet):
#     # queryset = APItest.objects.filter(model=['email', 'password'])