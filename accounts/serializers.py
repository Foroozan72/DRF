from rest_framework import serializers
from django.contrib.auth.models import User

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('your email contains admin .')

class UserRegistrSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(required=True , write_only ='True')

    class Meta:
        model = User
        fields = ('username','email' , 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True} ,
            'email' : {'validators':(clean_email ,)}
        }

    def create(self , validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
    
    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('you cant be admin')
        return value
    

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password and comfirm doesnt match')
        return data

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
    # username = serializers.CharField( required = True)
    # password =serializers.CharField(required=True , write_only ='True')
    # password2 =serializers.CharField(required=True , write_only ='True')
    # email = serializers.EmailField(required=True , validators =[clean_email] )

