from django.contrib.auth import authenticate, login, logout

from rest_framework import status, views
from rest_framework.response import Response

from .serializers import UserSerializer


class LoginView(views.APIView):
    @staticmethod
    def post(request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username of password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request=request, user=user)
        return Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    @staticmethod
    def get(request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
