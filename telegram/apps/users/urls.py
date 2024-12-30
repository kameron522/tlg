from django.urls import path
from . import views
from apps.messages import views as msg_views

app_name = 'users'

urlpatterns = [
    path('user-contacts/', views.Index.as_view()),
    path('create/', views.Store.as_view()),
    path('update/<str:username>/', views.Update.as_view()),
    path('delete/<str:username>/', views.Destroy.as_view()),
    path('del-user-img/<str:username>/', views.DelUserImg.as_view()),
    path('details/<str:username>/', views.Show.as_view()),
    path('search/', views.Search.as_view()),
    path('chats/<str:username>/', msg_views.Chat.as_view()),
]
