"""WebControlWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from Homepage.views import HomePage
from Robot.views import RobotIndex1,RobotIndex2,RobotIndex3
from Internet.views import InternetIndex1
from AI.views import AIIndex1,AIIndex2,AIIndex3
from VR_AR.views import VR_ARIndex1
from AboutMe.views import AboutMeIndex1

urlpatterns = {
    url(r'^admin/', admin.site.urls),
    url(r'^JoeWeb/home/$', HomePage),

    # Robot
    url(r'^JoeWeb/Robot/Index1/$', RobotIndex1),
    url(r'^JoeWeb/Robot/Index2/$', RobotIndex2),
    url(r'^JoeWeb/Robot/Index3/$', RobotIndex3),

    # Internet
    url(r'^JoeWeb/Internet/Index1/$', InternetIndex1),

    # Artificial Intelligence
    url(r'^JoeWeb/AI/Index1/$', AIIndex1),
    url(r'^JoeWeb/AI/Index2/$', AIIndex2),
    url(r'^JoeWeb/AI/Index3/$', AIIndex3),

    # VR-AR
    url(r'^JoeWeb/VR_AR/Index1/$', VR_ARIndex1),

    # About-me
    url(r'^JoeWeb/AboutMe/Index1/$', AboutMeIndex1),
}
