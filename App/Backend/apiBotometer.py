import botometer

rapid_api_key = "a5c7976279mshc4c1e60955473b3p13e6d5jsn553f9c2f7cd8"
twitter_app_auth = {
    'consumer_key': 'WnMbrFKacyv0ITQyXtuKSjeUt',
    'consumer_secret': 'RRvlf17vuvyaOKR1lm3DiUUg35m4AMlMfGR24t7CdZukFiGOIb',
    'access_token': '1169122850726453249-nzt2nFIkB4kd2PMMUU6sLz3eOZVvHK',
    'access_token_secret': '9nQ2TqBiAj7soc34ahcGyNekCfXDZ6WExWKJvuJ96Ct82',
}
boto_meter_object = botometer.Botometer(wait_on_ratelimit=True,
                                        rapidapi_key=rapid_api_key,
                                        **twitter_app_auth)


def check_account(name):
    return boto_meter_object.check_account(name)
