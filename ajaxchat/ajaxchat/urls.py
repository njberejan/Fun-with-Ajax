from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from chatterbox import views

router = routers.DefaultRouter()
router.register(r'chatterbox', views.ChatterboxViewSet)

urlpatterns = [
    # Examples:
    url(r'^home/', views.ChatterboxView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
