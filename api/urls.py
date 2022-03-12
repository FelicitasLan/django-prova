from django.urls import path, include
from .views import prova, getRoutes, MyTokenObtainPairView, get_user

from rest_framework_simplejwt.views import ( # for login
    TokenRefreshView,
)


urlpatterns = [
        path('prova/', prova),
        path('', getRoutes),

        path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('user/', get_user),
]