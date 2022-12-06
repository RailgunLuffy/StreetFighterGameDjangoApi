from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.PlayerApiView.as_view(), name='player-api'),
    path('last-player/', views.getLastPlayerApiView.as_view(), name='plast-player-api'),
]
urlpatterns = format_suffix_patterns(urlpatterns)