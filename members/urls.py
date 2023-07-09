from django.urls import path, include
from .views import *

app_name = 'members'

urlpatterns = [
    path('login/', login),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('logout/', logout)
]