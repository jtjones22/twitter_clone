from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from tweet.forms import AddTweetForm
from tweet.models import Tweet
from notification.models import Notification
from twitteruser.models import Profile
import re

# Create your views here.


@login_required
def add_tweet_view(request):
    html = 'add_tweet_form.html'
    users_list = [user.username for user in Profile.objects.all()]
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = Tweet.objects.create(
                body=data['body'],
                submitted_by=request.user
            )
            tweet.save()
            if '@' in data["body"]:
                users = re.findall(r"@([\w]+)", data["body"])
                for user in users:
                    if user in users_list:
                        alert = Notification.objects.create(
                            reciever=Profile.objects.get(username=user),
                            tweet=tweet
                        )
                        alert.save()
                        return HttpResponseRedirect(reverse('homepage'))
                    else:
                        messages.error(request, 'User does not exist!')
                else:
                    messages.error(request, 'User does not exist!')
    form = AddTweetForm()
    context = {'form': form}
    return render(request, html, context)


def tweet_detail(request, tweet_id):
    html = 'tweet_detail.html'
    tweet = Tweet.objects.get(id=tweet_id)
    context = {'tweet': tweet}
    return render(request, html, context)