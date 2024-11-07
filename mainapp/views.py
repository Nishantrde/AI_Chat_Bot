# api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from .models import User, Chat
from .serializers import UserSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.db import transaction, IntegrityError
from django.db import IntegrityError, transaction

# Registration 
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # see if user exists and if not returning status HTTP_400_BAD_REQUEST
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # creating user returning status HTTP_201_CREATED
        user = User.objects.create(username=username, password=make_password(password), tokens=4000)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

        # Attempt to create a new token, handling exceptions explicitly
        try:
            with transaction.atomic():
                # Delete any existing tokens for this user to avoid duplicates
                Token.objects.filter(user=user).delete()
                
                # Create a new token
                token = Token.objects.create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
                
        except IntegrityError as e:
            # Log the specific error message for debugging
            print("IntegrityError during token creation:", e)
            return Response(
                {"error": "Token generation failed due to a database integrity issue."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Chat_API
class ChatView(APIView):
    # Token authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        message = request.data.get("message")
        # See weather the user have sufficient toke and if not returning status HTTP_403_FORBIDDEN
        if user.tokens < 100:
            return Response({"error": "Insufficient tokens."}, status=status.HTTP_403_FORBIDDEN)

        # Deduct tokens
        user.tokens -= 100
        user.save()

        # Generate a dummy response (for simplicity)
        response_text = f"AI Response to: {message}."

        # Save the chat in the database
        chat = Chat.objects.create(user=user, message=message, response=response_text)
        
        return Response({
            "message": message,
            "response": response_text,
            "remaining_tokens": user.tokens
        }, status=status.HTTP_200_OK)

# Balance 
class TokenBalanceView(APIView):
    # Token authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # retuning the tokens left for the user and status HTTP_200_OK
        user = request.user
        return Response({
            "user" : user.username,
            "tokens": user.tokens
            }, status=status.HTTP_200_OK)

