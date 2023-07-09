from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardId.as_view()),
    path('<int:pk>/update', BoardFix.as_view()),
    path('<int:pk>/destroy', BoardDestroy.as_view()),
    path('<int:pk>/comments', BoardComment.as_view()),
]