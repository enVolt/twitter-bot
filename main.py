import tweepy
import authcred
import settings


def debug(s):
    if settings.debug:
        print s


class MyStream(tweepy.StreamListener):
    def on_connect(self):
        print "Connected to twitter stream"

    def on_status(self, status):
        print status.text.encode('UTF-8')
        print '\n'
        if status.user.screen_name in ignore_user_list:
            pass
        elif not status.retweeted_status:
            api.create_favorite(status.id_str)
            if status.retweeted_count > 3:
                api.retweet(status.id_str)

    def on_disconnect(self, notice):
        print notice


if __name__ == '__main__':
    ignore_user_list = None
    auth = tweepy.OAuthHandler(authcred.consumer_key, authcred.consumer_secret)
    auth.set_access_token(authcred.access_token, authcred.access_token_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStream()
    myStream = tweepy.Stream(api.auth,myStreamListener)
    myStream.filter(track=['#Wordpress'])
