from api.views import *
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('signup/', register_app),
    path('login/', login_app),
    path('get_income/<int:id>/', all_income),
    path('get_expense/<int:id>/', all_expense),
    path('add_income/', add_income),
    path('delete_income/<int:id>/', delete_income),
    path('add_expense/', add_expense),
    path('delete_expense/<int:id>/', delete_expense),
]
