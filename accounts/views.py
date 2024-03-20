from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html', {'user': request.user})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import login, logout
# from .serializers import SignupSerializer, LoginSerializer, UserProfileSerializer
# from django.contrib.auth.models import User

# class SignupAPIView(APIView):
#     def post(self, request):
#         serializer = SignupSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"user": UserProfileSerializer(user).data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginAPIView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             login(request, user)
#             return Response({"user": UserProfileSerializer(user).data}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         logout(request)
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class UserProfileAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserProfileSerializer(request.user)
#         return Response(serializer.data)

