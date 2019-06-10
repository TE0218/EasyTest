"""EasyTest URL Configuration

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
# from django.urls import path
from django.conf.urls import include
# from EasyTest.views import index
from EasyTest import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [

    url(r'admin/', admin.site.urls),
    url(r'^$', view=views.index),
    url(r'index/', view=views.index),
    url(r'^login_action/', view=views.login_action, name='login_action'),
    url(r'^logout/', view=views.logout, name='logout'),  # 退出
    url(r'^img_download/', view=views.img_download, name='img_download'),  # 下载图片

    url(r'^base/', include("base.urls")),

    url(r'^favicon.ico$', RedirectView.as_view(url=r'/static/img/favicon.png')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error
