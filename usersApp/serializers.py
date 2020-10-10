from rest_framework import serializers
from django.db.models import Q
from . import models


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = models.CustomUser
        fields = ('name', 'email', 'username', 'photo', 'password', 'password2')
        extra_kwargs= {
            'password' : {'write_only': True}
        }
        
    def save(self):
        user = models.CustomUser(
                name=self.validated_data['name'],
                email=self.validated_data['email'],
                username=self.validated_data['username'],
                photo =self.validated_data['photo'],
        )
        #name = self.validated_data['name']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']


        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        
        user.set_password(password)
        user.save()

        return user

class userLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    usernameOremail = serializers.CharField(label='Username', required=True, allow_blank=False)
    #email = serializers.EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model=models.CustomUser
        fields=[
            'usernameOremail',
            'password',
            'token'
        ]
        extra_kwargs= {
            'password' : {'write_only': True}
        }

    def validate(self, data):
        user_obj = None
        email = data.get("usernameOremail", None)
        #username = data.get("username", None)
        password = data['password']

        if not email:
            raise serializers.ValidationError("A username or email is required to login :)")
        
        user = models.CustomUser.objects.filter(
                Q(email=email) |
                Q(username=email)
            ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username/ email is not valid")
        
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect credentials please try again")
        
        data['token'] = "SOME RANDOM TOKEN"

        return data



