from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('medicinelist', views.medicine_list, name='medicine_list'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('edit/<int:pk>/', views.edit_medicine, name='edit_medicine'),
    path('delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),

    # 🔥 This line fixes your issue
    path('accounts/login/', auth_views.LoginView.as_view(template_name='store/login.html')),
]
