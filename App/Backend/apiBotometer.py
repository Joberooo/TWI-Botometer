import botometer

from Backend.globalSettings import rapid_api_key, twitter_app_auth

boto_meter_object = botometer.Botometer(wait_on_ratelimit=True,
                                        rapidapi_key=rapid_api_key,
                                        **twitter_app_auth)


def check_account(name):
    return boto_meter_object.check_account(name)
