from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from tweet.models import Tweet
from twitteruser.models import Profile
from notification.models import Notification
from twitteruser.get_tweets import get_tweets

# Create your views here.


@login_required
def index(request):
    html = 'index.html'
    user = request.user
    tweets = get_tweets(user)
    alerts = Notification.objects.filter(reciever=request.user.id)
    num_of_alerts = []
    for alert in alerts:
        if alert.read is False:
            num_of_alerts.append(alert)
    context = {
        'user': user,
        'tweets': tweets,
        'notification': alerts,
        'num_of_alerts': num_of_alerts,
        }
    return render(request, html, context)


def user_profile(request, username):
    html = 'user_profile.html'
    profile = Profile.objects.get(username=username)
    tweets = Tweet.objects.filter(submitted_by=profile.id)
    tweets = tweets.order_by('-time')
    context = {
        'user': profile,
        'tweets': tweets
        }
    return render(request, html, context)


@login_required
def follow_user(request, user_id):
    user = Profile.objects.get(id=user_id)
    username = user.username
    request_user = request.user
    request_user.following.add(user)
    user.save()
    return HttpResponseRedirect(reverse('user_profile', args=(username,)))


@login_required
def unfollow_user(request, user_id):
    user = Profile.objects.get(id=user_id)
    username = user.username
    request_user = request.user
    request_user.following.remove(user)
    user.save()
    return HttpResponseRedirect(reverse('user_profile', args=(username,)))