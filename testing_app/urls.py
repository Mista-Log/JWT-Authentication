from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)
from . import views



urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('test/', views.TestingList.as_view()),
    path('test/<int:pk>', views.TestingDetails.as_view()),
    
    path('company', views.CompanyList.as_view()),
]
