from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login_view.as_view(), name='user-login'),
    path('logout/', views.logout_view.as_view(), name='user-logout'),
    path('singup/', views.singup_view.as_view(), name='user-singup'),
    path('profile/<int:user_id>', views.profile_view.as_view(), name='user-profile'),
]