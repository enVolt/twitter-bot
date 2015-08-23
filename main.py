import tweepy
import authcred
import settings


def debug(s):
    if settings.debug:
        print s



def addToIgnoreList(screen_name):
    f = open('ignorelist.txt','a')
    f.write(screen_name+'\n')
    f.close()
    global ignore_user_list
    ignore_user_list += [screen_name]


class MyStream(tweepy.StreamListener):
    def on_connect(self):
        print "Connected to twitter stream"

    def on_status(self, status):
        print status.text.encode('UTF-8')
        print '\n'
        if status.user.friends_count > 5000:
            addToIgnoreList(status.user.screen_name)
        elif status.user.screen_name in ignore_user_list:
            pass
        else:
            api.create_favorite(status.id_str)

    def on_disconnect(self, notice):
        print notice


if __name__ == '__main__':
    ignore_user_list = []
    auth = tweepy.OAuthHandler(authcred.consumer_key, authcred.consumer_secret)
    auth.set_access_token(authcred.access_token, authcred.access_token_secret)
    api = tweepy.API(auth)
    myStreamListener = MyStream()
    myStream = tweepy.Stream(api.auth,myStreamListener)
    myStream.filter(track=['#Wordpress'])
