from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from .models import User  # Import your User model

class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        
        try:
            token_type, token = auth_header.split(' ')
            if token_type.lower() != 'bearer':
                raise AuthenticationFailed('Invalid token header')
        except ValueError:
            raise AuthenticationFailed('Invalid token header')

        try:
            # Decode the JWT token
            access_token = AccessToken(token)
            user_id = access_token.get('user_id')
            if not user_id:
                raise AuthenticationFailed('User ID not found in token')

            try:
                # Retrieve the user associated with the token
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                raise AuthenticationFailed('User not found')

            return (user, token)

        except Exception as e:
            raise AuthenticationFailed(f'Invalid token: {str(e)}')

    def authenticate_header(self, request):
        return 'Bearer'
