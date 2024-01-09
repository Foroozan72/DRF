from django.urls import path
from . import views
from rest_framework.authtoken import views as views_auth
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



app_name='accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    # path('api-token-auth/', views_auth.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = routers.SimpleRouter()
router.register('user' , views.UserViewSet)

urlpatterns += router.urls




# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNDc4NTI2NywiaWF0IjoxNzA0Njk4ODY3LCJqdGkiOiJkNWZiZDI5NzZlZDc0YmI1OWUxZWI4N2U3YWQyNmRkOSIsInVzZXJfaWQiOjE1fQ.bEmc-wQZ6EDeDs3EcEPoq5283pV70d2DsNoMXXjUnMM",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0Njk5MTY3LCJpYXQiOjE3MDQ2OTg4NjcsImp0aSI6Ijk0NzU5YWJmZTY2YzRhYzU5MmQ4NWQzMzMyNTA4ODE1IiwidXNlcl9pZCI6MTV9.qc-JdTWo3ca4p-l17RWYVsJW0q90lJUVWB7IIiQ0yNY"
# }