from functools import total_ordering

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def login_app(request):
    try:
        username = request.data['username']
        user_ins = User.objects.get(username=username)
        serializer = UserSerializer(user_ins)

        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def all_income(request, id):
    try:
        user_ins = User.objects.get(pk=id)
        income_ins = Income.objects.filter(user=user_ins)
        serializer = IncomeSerializer(income_ins, many=True)

        total_income = 0

        for item in income_ins:
            total_income = total_income + item.amount

        print(total_income)

        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data,
            'total': total_income
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def all_expense(request, id):
    try:
        user_ins = User.objects.get(pk=id)
        expense_ins = Expense.objects.filter(user=user_ins)
        serializer = ExpenseSerializer(expense_ins, many=True)

        total_expense = 0

        for item in expense_ins:
            total_expense = total_expense + item.amount

        print(total_expense)

        return Response({
            'status': status.HTTP_200_OK,
            'data': serializer.data,
            'total': total_expense
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add_income(request):
    try:
        user = request.data['user_id']
        amount = request.data['amount']
        title = request.data['title']

        income_ins = Income(
            user = User.objects.get(pk=user),
            amount = amount,
            title = title
        )

        income_ins.save()

        return Response({
            'status': status.HTTP_201_CREATED,
            'msg': "Income added successfully!"
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def delete_income(request, id):
    try:
        income_ins = Income.objects.get(pk=id)
        income_ins.delete()

        return Response({
            'status': status.HTTP_200_OK,
            'msg': "Income deleted successfully!"
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def add_expense(request):
    try:
        user = request.data['user_id']
        amount = request.data['amount']
        title = request.data['title']

        expense_ins = Expense(
            user = User.objects.get(pk=user),
            amount = amount,
            title = title
        )

        expense_ins.save()

        return Response({
            'status': status.HTTP_201_CREATED,
            'msg': "Expense added successfully!"
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def delete_expense(request, id):
    try:
        expense_ins = Expense.objects.get(pk=id)
        expense_ins.delete()

        return Response({
            'status': status.HTTP_200_OK,
            'msg': "Expense deleted successfully!"
        })

    except Exception as error:
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'msg': str(error)
        })





