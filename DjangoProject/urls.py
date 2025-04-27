"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, reverse
from django.views.generic import RedirectView
from django.contrib import admin
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'reservations': reverse('reservation-list-create', request=request),
        'reviews':      reverse('review-list-create',  request=request),
    })

urlpatterns = [
       path('admin/', admin.site.urls),
    path('', RedirectView.as_view(
        url='/api/reservations/', permanent=False
    )),
    path('api/reservations/', include('reservations.urls')),
    path('api/reviews/', include('reviews.urls')),
]


