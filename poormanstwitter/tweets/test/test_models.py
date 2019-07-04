from django.test import TestCase
from ..models import Tweet


class TweetTest(TestCase):
    """ Test module for Tweet model """

    def setUp(self):
        Tweet.objects.create(name='Marlon Brando', message='Poor Mans Twitter using VUE and Django')

    def test_tweet_message(self):
        tweet_instance = Tweet.objects.get(name='Marlon Brando')
        self.assertGreater(len(tweet_instance.message), 0)
        self.assertLess(len(tweet_instance.message), 50)