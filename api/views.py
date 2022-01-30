from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# signup view
@api_view(['POST'])
def register_app(request):
    try:
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        # confirm_password = request.data['confirm_password']

        user_ins = User(
            username = username,
            email = email
        )

        user_ins.set_password(password)
        user_ins.save()

        return Response({
            'status': status.HTTP_201_CREATED,
            'msg': 'User created seccessfully!'
        })
    
    
    except Exception as error:
        return Response({
            'status':status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })


