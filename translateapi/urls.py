from django.urls import include, path
from rest_framework import routers
from .views import (
    TranslateApiView,IzoxTemplate
)

router = routers.SimpleRouter()


urlpatterns = [
    path('', TranslateApiView.as_view()),
    path('apii/', IzoxTemplate.as_view())
]