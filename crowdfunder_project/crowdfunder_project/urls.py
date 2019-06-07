"""crowdfunder_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from crowdfunder_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/new', new_project, name='new_project'),
    path('', root),
    path('home/', home_page, name='home_page'),
    path('create/', create_project, name='create_project'),
    path('projects/<int:id>/', show_project, name='show_project'),
    # path('projects/', show_project, name='projects_page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
]
