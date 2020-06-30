from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework import routers
from kartriderTMI import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('wisesaying', views.WiseSayingView, 'wisesaying')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(router.urls)),
]