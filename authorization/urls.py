from django.urls import path
from django.contrib.auth import views
from authorization.views import login_user, signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', views.LogoutView.as_view(next_page='index'), name='logout'),
]
