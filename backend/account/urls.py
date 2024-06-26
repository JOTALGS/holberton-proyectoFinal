from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('me/', views.me, name='me'),
    path('users/<int:id>/', views.users, name='me'),
    path('signup/', views.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('editpassword/', views.editpassword, name='editpassword'),
    path('suggestions/', views.suggest_users, name='suggestions'),
    path('friends/<int:pk>/', views.friends, name='friends'),
    path('friends/<int:pk>/request/', views.send_friendship_request, name='send_friendship_request'),
    path('friends/<int:pk>/<str:status>/', views.handle_request, name='handle_request'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]