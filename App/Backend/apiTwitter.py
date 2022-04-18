import twython.exceptions
from twython import Twython

from Backend.globalSettings import twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret

t = Twython(app_key=twitter_app_key,
            app_secret=twitter_app_secret,
            oauth_token=twitter_oauth_token,
            oauth_token_secret=twitter_oauth_token_secret)


def get_user_from_twitter(account_name):
    return t.show_user(screen_name=account_name)


def get_user_name_from_id(random_id):
    try:
        user = t.show_user(id=random_id)
        return user['screen_name']
    except twython.exceptions.TwythonError:
        return ''
