from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Para mostrar usuarios (listar y ver detalle)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "bio"]

# Para registrar un usuario nuevo
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        # Usamos create_user de Django para que la password se guarde encriptada
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user
