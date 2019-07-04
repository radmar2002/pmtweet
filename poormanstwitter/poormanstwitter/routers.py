from rest_framework import routers
from tweets.viewsets import TweetViewSet

router = routers.DefaultRouter()

router.register(r'tweet', TweetViewSet)