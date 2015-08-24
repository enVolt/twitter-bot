import tweepy
import authcred
import settings


def debug(s):
    if settings.debug:
        print s


def addToIgnoreList(screen_name):
    f = open(settings.user_file, 'a')
    f.write(screen_name + '\n')
    f.close()


def updateSinceID(id_str):
    sinceidfile = open(settings.since_id_file, 'w+')
    sinceidfile.write(id_str)
    sinceidfile.close()


def getSinceID():
    sinceidfile = open(settings.since_id_file, 'r')
    since_id = sinceidfile.read()
    sinceidfile.close()
    return since_id


def addToUnfollowList(id_str):
    userfile = open(settings.user_file, 'a+')
    userfile.write(id_str + '\n')
    userfile.close()


if __name__ == '__main__':
    ignore_user_list = []
    auth = tweepy.OAuthHandler(authcred.consumer_key, authcred.consumer_secret)
    auth.set_access_token(authcred.access_token, authcred.access_token_secret)
    api = tweepy.API(auth)
    # myStreamListener = MyStream()
    # myStream = tweepy.Stream(api.auth,myStreamListener)
    # myStream.filter(track=['#Wordpress'])

    # q = settings.search_qeury
    debug('Search Query = ' + q)
    q = raw_input()
    for status in tweepy.Cursor(api.search, q = q, since_id = getSinceID()).items(20):
        last_status = status
        try:
            api.create_friendship(status.user.screen_name)
        except:
            pass
        finally:
            addToIgnoreList(status.user.screen_name)

        try:
            api.create_favorite(status.id_str)
        except:
            pass


    updateSinceID(last_status.id_str)
