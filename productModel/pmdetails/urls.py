from django.urls import include, path

from .views import *

# app_name = 'curd'

router = routers.DefaultRouter()
router.register(r'students', StudentCurd, basename="students")
urlpatterns = [
    path("",include(router.urls))
]