from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'myapp'

urlpatterns = [
    path('', views.root_view, name='root'),  # Add this line at the top
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='myapp:login'), name='logout'),
    path('route/', views.route_view, name='route'),
]