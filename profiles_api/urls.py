from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)#no es necesario definir un basename pq estamos llamando a los objetos en el model viewset

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),#cargamos la clase como funcion con as_view
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)), #encuentra los urls necesarios para la funcion del viewset

]
