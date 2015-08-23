import tweepy
import settings

class MyStream(tweepy.StreamListener):
    def on_connect(self):
        print "Connected to twitter stream"

    def on_status(self, status):
        print status.text

    def on_disconnect(self, notice):
        print notice

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
    auth.set_access_token(settings.access_token, settings.access_token_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStream()
    myStream = tweepy.Stream(api.auth,myStreamListener)
    myStream.filter(track='ThankYouSanga')
