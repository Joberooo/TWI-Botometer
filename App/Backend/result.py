class Result:
    def __init__(self, botometer_object, user_name, name, description, image):

        if botometer_object == "hasNoTimeline":
            self.all_features = 0
            self.astroturf = 0
            self.fake_follower = 0
            self.financial = 0
            self.other = 0
            self.overall = 0
            self.self_declared = 0
            self.spammer = 0
            self.majority_lang = 0
            self.screen_name = user_name
            self.has_timeline = False
            self.account_exist = True
            self.name = name
            self.description = description
            self.image = image
        elif botometer_object == "doesntExist":
            self.all_features = 0
            self.astroturf = 0
            self.fake_follower = 0
            self.financial = 0
            self.other = 0
            self.overall = 0
            self.self_declared = 0
            self.spammer = 0
            self.majority_lang = 0
            self.screen_name = user_name
            self.has_timeline = False
            self.account_exist = False
            self.name = name
            self.description = description
            self.image = image
        else:
            self.all_features = botometer_object['display_scores']['english']['overall']
            self.astroturf = botometer_object['display_scores']['universal']['astroturf']
            self.fake_follower = botometer_object['display_scores']['universal']['fake_follower']
            self.financial = botometer_object['display_scores']['universal']['financial']
            self.other = botometer_object['display_scores']['universal']['other']
            self.overall = botometer_object['display_scores']['universal']['overall']
            self.self_declared = botometer_object['display_scores']['universal']['self_declared']
            self.spammer = botometer_object['display_scores']['universal']['spammer']
            self.majority_lang = botometer_object['user']['majority_lang']
            self.screen_name = botometer_object['user']['user_data']['screen_name']
            self.has_timeline = True
            self.account_exist = True
            self.name = name
            self.description = description
            self.image = image
