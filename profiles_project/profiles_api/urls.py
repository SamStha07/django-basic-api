from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . views import HelloApiView, HelloViewSet

# bcz of ViewSet with Routers
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-apiview/', HelloApiView.as_view()),
    path('', include(router.urls)),  #bcz of viewset
]
