from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import Admin
import jwt
import datetime
from .serializers import AdminSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# View to handle admin login
class AdminLoginView(APIView):
    def post(self, request):
        # Get email and password from the request data
        email = request.data['email']
        password = request.data['password']

        try:
            # Check if the admin exists with the given email
            user = Admin.objects.get(email_admin=email)
        except Admin.DoesNotExist:
            raise AuthenticationFailed('User not found!')

        # Check if the provided password matches the stored password for the admin
        if not user.password_admin == password:
            raise AuthenticationFailed('Incorrect password')

        # Generate a JWT token with user ID, expiration time, and issued at time as payload
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        print('Generated Token:', token)

        # Set the JWT token as an HTTP-only cookie and return it in the response
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

# View to retrieve admin details
class AdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Get the JWT token from the request cookies
            token = request.COOKIES.get('jwt')

            if not token:
                raise AuthenticationFailed('Unauthenticated!')

            print('Received Token:', token)

            # Decode the JWT token to get the user ID
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = Admin.objects.filter(id=payload['id']).first()

            if not user:
                raise AuthenticationFailed('User not found!')

            # Check if the user has permission to access the admin panel
            if not user.has_permission_to_access_admin_panel():
                raise PermissionDenied('Access to admin panel is not allowed!')

            # Serialize the user data and return it in the response
            serializer = AdminSerializer(user)
            return Response(serializer.data)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired!')

        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token!')

        except (AuthenticationFailed, PermissionDenied) as e:
            return Response({'detail': str(e)}, status=403)

# View to handle admin logout
class LogoutView(APIView):
    def post(self, request):
        # Create a response to delete the JWT token cookie
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
