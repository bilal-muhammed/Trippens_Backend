"""tuour_managment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [


    # path('admin/', admin.site.urls),
    path('admin-side/', include('admin_requirments.urls')),
    path('trippens/', include('trippens.urls')),
    path('diksha/', include('diksha.urls')),
    path('gossip/', include('gossip.urls')),
    path('team_adventure/', include('team_adventure.urls')),
    path('user_managment/', include('user_managment.urls')),
    path(' telecaller/', include('telecaller.urls')),




# JWT Authentication URL'S
    # path("token/", TokenObtainPairView.as_view(), name="obtain_token"),
   
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
