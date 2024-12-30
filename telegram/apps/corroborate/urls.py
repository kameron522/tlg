from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken_views


app_name = 'corroborate'

urlpatterns = [
    path('login/', authtoken_views.obtain_auth_token),
    path('logout/', views.Destroy.as_view()),
]
