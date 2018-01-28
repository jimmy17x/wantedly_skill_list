"""wantedly_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import refresh_jwt_token
from django.conf.urls import include
from wantedly_webapp.views.UserDetailsView import DetailsView
from wantedly_webapp.views import AllViews as wantedly_app_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", TemplateView.as_view(template_name='index.html')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/login/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^user/$', DetailsView.as_view(), name='rest_user_details'),
    url(r'^', include('api.urls')),
    url(r'^api/v1/skills/$', wantedly_app_views.skill_collection),
    url(r'^api/v1/skills/(?P<pk>[0-9]+)$', wantedly_app_views.skill_element),
    url(r'^api/v1/user/skills/(?P<pk>[0-9]+)$', wantedly_app_views.user_skill_collection),
    url(r'^api/v1/user/skill/upvotes/(?P<pk>[0-9]+)$', wantedly_app_views.user_skill_upvotes),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
