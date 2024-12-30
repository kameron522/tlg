from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('all-messages/', views.Index.as_view()),
    path('send-message/<str:username>/', views.Store.as_view()),
    path('edit-message/<int:message_id>/', views.Update.as_view()),
    path('delete-message/<int:message_id>/', views.Destroy.as_view()),
    path('del-mgs-img/<int:message_id>/', views.DelMsgImg.as_view()),
    path('replay/<int:message_id>/', views.Replay.as_view()),
    path('search/', views.Search.as_view()),
]
