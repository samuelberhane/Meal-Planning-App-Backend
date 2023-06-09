"""
URL configuration for plateplanbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from .users import MealUsers
from .messages import send_email



urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/',send_email),
    path('api/meals/', include('mealapp.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



websocket_urlpatterns = [
    path('ws/meal/', MealUsers.as_asgi()),
]


urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name="index.html"))]

# add custom text in admin page
admin.site.index_title = "Plate Plan"
admin.site.site_header = "Plate Plan Admin"
admin.site.site_title = "Site Meal Planner"