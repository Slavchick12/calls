"""Urls for Phones application."""


from django.urls import include, path
from phones import views
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register(prefix='connection', viewset=views.ConnectionViewSet, basename='connections')
router_v1.register(prefix='audio', viewset=views.AudioViewSet, basename='audio')
router_v1.register(prefix='numbers', viewset=views.NumbersViewSet, basename='numbers')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/call/', views.Calls.as_view(), name='call'),
]
