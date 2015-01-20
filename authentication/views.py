import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.admin import csrf_protect_m
 
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from pyreadline.console.console import Console
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

def create(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
        Account.objects.create_user(**serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    
    return Response({
    'status': 'Bad request',
    'message': 'Account could not be created with received data.'
    }, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class LoginView(views.APIView):
    permission_classes = (AllowAny,)
    
    
   
    def post(self, request, format=None):
            
        s = str(request.DATA)
        s = s.replace("u'", "\"");
        s= s.replace("'", "\""); 
        
        print s
        
        data = json.loads(s)
        
        email = data.get('email', None)
        password = data.get('password', None)
        
        account = authenticate(email=email, password=password)
        

        if account is not None:
            #Console.write(self, " logged in " + account)
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)