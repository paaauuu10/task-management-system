from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()

# -----------------------------
# API Endpoints
# -----------------------------

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# List users
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# User detail
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# JWT Login
class LoginView(TokenObtainPairView):
    pass

# JWT Refresh
class TokenRefreshViewCustom(TokenRefreshView):
    pass

# Current user
class UserMeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Logout with token blacklist
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------
# Frontend Views
# -----------------------------

def home_view(request):
    return redirect("login")  # redirect root to login

def login_view(request):
    message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # En lugar de redirigir, mostramos un mensaje simple
            message = f"You are logged in as {user.username}!"
            return render(request, "users/login_success.html", {"message": message})
        else:
            message = "Invalid username or password"
    return render(request, "users/login.html", {"error": message})

def register_view(request):
    message = None
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            message = "Username already taken"
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            message = f"Account created for {user.username}! You can now login."
            return render(request, "users/login_success.html", {"message": message})
    return render(request, "users/register.html", {"error": message})

def logout_view(request):
    logout(request)
    return redirect("login")

def home_view(request):
    return redirect("login")

