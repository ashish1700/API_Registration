from rest_framework import serializers
from endpoint.models import APItest, User
from rest_framework.response import Response
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from endpoint.utils import Util


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
 

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','email','name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, write_only= True )
    password2 = serializers.CharField(max_length=255, write_only= True )
    class Meta:
        fields = ['password', 'password2']
        
        def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')
            user = self.context.get('user')
            if password != password2:
                raise serializers.ValidationError("password and confirm password doesnt match")
            user.set_password(password)
            user.save()
            return attrs

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 255) 
    class Meta:
        fields = ['email']
        
        
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email = email)
            # uid = urlsafe_based64_encode(force_bytes(user.id))
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:3000/api/v1/reset/'+uid+'/'+token
            print('Password Reset Link', link)
            # send Email
            body = 'Click Following Link to reset your password '+link
            data = {
                'subject':'reset your password',
                'body':body,
                'to_email':user.email
            }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationErr("you are not registeered User")


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, write_only= True )
    password2 = serializers.CharField(max_length=255, write_only= True )
    class Meta:
        fields = ['password', 'password2']
        
        def validate(self, attrs):
            try:
                password = attrs.get('password')
                password2 = attrs.get('password2')
                uid = self.context.get('uid')
                token = self.context.get('token')
                if password != password2:
                    raise serializers.ValidationError("password and confirm password doesnt match")
                id = smart_str(urlsafe_base64_decode(uid))
                user = User.objects.get(id=id)
                if not PasswordResetTokenGenerator().check_token(user, token):
                    raise ValueError('Token is not valid or expired') 
                user.set_password(password)
                user.save()
                return attrs
            except DjangoUnicodeDecodeError as identifier:
                PasswordResetTokenGenerator().check_token(user,token)
                raise ValidationError('token is not valid or Expired')




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

