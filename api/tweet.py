import settings
import tweepy

def sendTweet(user, tweet):
    
    social_auth_user = user.social_auth.get()
    if user.is_authenticated() is True and social_auth_user is not None:
        access_token_strings = social_auth_user.extra_data['access_token'].split('&')
        access_token_key = access_token_strings[1][12:]
        access_token_secret = access_token_strings[0][19:]
    else:
        return False
    
    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(access_token_key, access_token_secret)
    
    twitterapi = tweepy.API(auth)
    
    twitterapi.update_status(tweet)
    
    return True