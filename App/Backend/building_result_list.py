import botometer
from Backend import apiBotometer
from Backend.result import Result


def add_to_list(user_name, results_list):
    if len(results_list) < 1:
        results_list.insert(0, get_result(user_name))
    else:
        if any(user_name == result.screen_name for result in results_list):
            pass
        else:
            results_list.insert(0, get_result(user_name))


def get_result(user_name):
    if user_name is not None:
        try:
            return Result(apiBotometer.check_account(user_name), user_name)
        except botometer.NoTimelineError:
            return Result("hasNoTimeline", user_name)
        except botometer.TweepError:
            return Result("doesntExist", user_name)
    else:
        return None
