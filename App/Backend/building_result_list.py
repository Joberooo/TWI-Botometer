import random

import botometer
import twython.exceptions

from Backend import apiBotometer
from Backend.apiTwitter import get_user_from_twitter, get_user_name_from_id
from Backend.result import Result


def add_to_list(user_name, results_list):
    if len(results_list) < 1:
        results_list.insert(0, get_result(user_name))
    else:
        if any(user_name == result.screen_name for result in results_list):
            pass
        else:
            results_list.insert(0, get_result(user_name))


def delete_from_list(user_name, results_list):
    if len(results_list) >= 1:
        for result in results_list:
            if user_name == result.screen_name:
                results_list.remove(result)
                break


def add_random_to_list(results_list):
    user_name = ''
    while user_name == '':
        x = random.randint(0, 5000000000)
        user_name = get_user_name_from_id(x)
        if user_name != '':
            add_to_list(user_name, results_list)


def get_result(user_name):
    if user_name is not None:
        try:
            user = get_user_from_twitter(user_name)
            try:
                return Result(apiBotometer.check_account(user_name), user_name, user['name'],
                              user['description'], user['profile_image_url_https'])
            except botometer.NoTimelineError:
                return Result("hasNoTimeline", user_name, user['name'] + " - NoTimelineError",
                              user['description'], user['profile_image_url_https'])
            except botometer.TweepError:
                return Result("doesntExist", user_name, user['name'] + " - doesntExist",
                              user['description'], user['profile_image_url_https'])
        except twython.exceptions.TwythonError:
            return Result("doesntExist", user_name, user_name + " - doesntExist", '', '')
    else:
        return None
