# Url Patterns for the project!!

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('client/<uuid:client_id>/', views.client_details, name='client_details'),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('application/', views.application, name="application"),
    path('loantracker/', views.loantracker, name="loantracker"),
    path('kpichooser/', views.kpichooser, name="kpichooser"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)