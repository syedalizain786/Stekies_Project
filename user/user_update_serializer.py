import re
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {field: {'required': False} for field in fields}
    
    
    def validate(self, data):
        if 'password' in data and data['password']:
            pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&])[A-Za-z\d#@$!%*?&]{8,}$')
            if not pattern.match(data['password']):
                raise serializers.ValidationError({
                    'password': "Password must be at least 8 characters long, contain at least one uppercase letter, "
                                "one lowercase letter, one number, and one special character including the # symbol."
                })
            data['password'] = make_password(data['password'])
        return super().validate(data)