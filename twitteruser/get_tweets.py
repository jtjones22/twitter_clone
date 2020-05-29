from tweet.models import Tweet
from itertools import chain


def get_tweets(user):
    following = user.following.all()
    user_tweets = Tweet.objects.filter(submitted_by=user)
    following_tweets = Tweet.objects.filter(submitted_by__in=following)
    tweets = sorted(list(chain(user_tweets, following_tweets)),
                    key=lambda tweet: tweet.time, reverse=True)
    return tweets
