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
    path('search', search_project, name ='search_project'), 
    path('create/', create_project, name='create_project'),
    path('projects/<int:id>/', show_project, name='show_project'),
    path('projects/<int:id>/add_reward', add_reward, name='add_reward'),
    path('projects/<int:id>/save_reward', save_reward, name='save_reward'),
    path('donate/<int:id>/', donate_reward, name='donate_reward'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('myprofile/', my_profile, name='my_profile'),
    path('project/update/<int:id>/', update_project, name='update_project'),
    path('projects/<int:id>/add_comment', save_comment, name='save_comment'),
]
