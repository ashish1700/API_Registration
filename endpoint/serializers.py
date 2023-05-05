from rest_framework import serializers
from endpoint.models import APItest, User
from rest_framework.response import Response

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class APItestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APItest
        fields = ['id','name','image','email','age','mobileno','password']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only= True)
    class Meta:
        model = User
        fields= ['email','name','password','password2','tc']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesnt match")
        return attrs
    
    #this is been done because we have made here custom models
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
        
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = ['email','password']
 














# class NewUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Register
#         fields = ["id", "first_name", "last_name", "username"]
 
 
 
# class RegisterSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required=True,validators=[UniqueValidator(queryset=Register.objects.all())])
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = Register
        
#         fields = ('username', 'password', 'password2','email', 'first_name', 'last_name')
#         extra_kwargs = {'first_name': {'required': True},'last_name': {'required': True}}
    
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})
#         return attrs
    
#     def create(self, validated_data):
#         user = Register.objects.create(username=validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'])
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
 
 
 
        
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = APItest
#         fields = ['email','password']

