"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from twitteruser.views import index, user_profile, follow_user, unfollow_user
from authentication.views import loginview, logoutview, signupview
from tweet.views import add_tweet_view, tweet_detail
from notification.views import notification_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('signup/', signupview, name='signup'),
    path('addtweet/', add_tweet_view, name='add_tweet'),
    path('tweet/<int:tweet_id>', tweet_detail, name='tweet_detail'),
    path('profile/<str:username>', user_profile, name='user_profile'),
    path('follow/<int:user_id>', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>', unfollow_user, name='unfollow_user'),
    path('notification/', notification_view, name='notification'),






]
