from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer


@api_view(['Post'])

def login_api(request):
    _serializer =AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=true)
    user =serializer.validated.dat['user']

    created,token=AuthToken.objects.create(user)
    
    return Respons({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    }

    )