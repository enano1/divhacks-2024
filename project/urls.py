from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('application/', views.application, name="application"),
    path('loantracker/', views.loantracker, name="loantracker"),
    path('kpichooser/', views.kpichooser, name="kpichooser"),


    path('submit1/', views.submit1, name="submit1"),
    path('submit2/', views.submit2, name="submit2"),
    path('confirmation/', views.confirmation, name="confirmation"),

    #Login and Logout Functionality
    path('loginpage/', views.custom_login, name='loginpage'),  # Custom login view
    path('register/', views.register, name='register'),

    path('currentloans/', views.current_loans, name='currentloans'),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
