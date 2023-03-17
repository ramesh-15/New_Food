from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import SignUpSerializer, LoginSerializer,DonateFoodSerializer
from .models import DonarUser,Users_donations
from django.contrib.auth import login
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.conf import settings
from django.core.mail import send_mail
import random
import string
# passcode
def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password

class SignUpView(generics.CreateAPIView):
    queryset = DonarUser.objects.all()
    serializer_class = SignUpSerializer
    def post(self,request):
        
        data = request.data.copy()
        otp = passcode()
        data['passcode']=otp
        serializer= self.get_serializer(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    
     # smtp passcode
        subject = 'Passcode Varification code '
        message = f' Hi  your passcode : {otp}thanks for Registering Helping Hands...'
        sender = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender, [data['email']])
        return Response({'success': True}, status=status.HTTP_200_OK)
    


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Use Django's login method to log the user in.
            login(request, user)
            return Response({'success': True}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Donar 

class DonarFoodView(ModelViewSet):
    queryset = Users_donations.objects.all()
    serializer_class = DonateFoodSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
# class DonarCart(ModelViewSet):
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     # print(request.user)
    # queryset = Users_donations.objects.filter( )

