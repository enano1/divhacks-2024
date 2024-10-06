from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('application/', views.application, name="application"),
    path('loantracker/', views.loantracker, name="loantracker"),
    path('kpichooser/', views.kpichooser, name="kpichooser"),


    path('submit1/', views.submit1, name="submit1"),
    path('submit2/', views.submit2, name="submit2"),
    path('confirmation/', views.confirmation, name="confirmation"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
