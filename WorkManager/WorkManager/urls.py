"""WorkManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TaskManager.views import page, connection, add_project, display_projects
from TaskManager.views import display_mine, display1, project_detail

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', page),
	#url(r'^index$', page, name="public_index"),
	#url(r'^connection$', connection, name="public_conection"),
	url(r'^index$', page, name="public_index"),
    url(r'^add$', add_project),
    url(r'^display$', display_projects),
    url(r'^mine$', display_mine),
    url(r'^one$', display1),         
	url(r'^connection$', connection, name="public_connection"),
    url(r'^detail(?P<pk>\d+)$', project_detail, name='project_detail'),
    url(r'^detail/(\d{1})/$', project_detail)    
]
