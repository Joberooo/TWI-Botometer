from flask import Flask, render_template

from Backend import apiBotometer

app = Flask(__name__)


class Result:
    def __init__(self, all_features, astroturf, fake_follower, financial, other, overall, self_declared, spammer,
                 majority_lang, id_str, screen_name):
        self.all_features = all_features
        self.astroturf = astroturf
        self.fake_follower = fake_follower
        self.financial = financial
        self.other = other
        self.overall = overall
        self.self_declared = self_declared
        self.spammer = spammer
        self.majority_lang = majority_lang
        self.id_str = id_str
        self.screen_name = screen_name


@app.route("/checkAccount")
def check_accountOne():
    return render_template("checkAccount.html", result=None)


@app.route("/checkAccount/<user_name>")
def check_accountTwo(user_name=None, result_obj=None):
    if user_name is not None:
        result = apiBotometer.check_account(user_name)

        all_features = result['display_scores']['english']['overall']
        astroturf = result['display_scores']['universal']['astroturf']
        fake_follower = result['display_scores']['universal']['fake_follower']
        financial = result['display_scores']['universal']['financial']
        other = result['display_scores']['universal']['other']
        overall = result['display_scores']['universal']['overall']
        self_declared = result['display_scores']['universal']['self_declared']
        spammer = result['display_scores']['universal']['spammer']
        majority_lang = result['user']['majority_lang']
        id_str = result['user']['user_data']['id_str']
        screen_name = result['user']['user_data']['screen_name']

        result_obj = Result(all_features, astroturf, fake_follower, financial, other, overall, self_declared,
                           spammer, majority_lang, id_str, screen_name)

    else:
        result = None
    return render_template("checkAccount.html",
                           result=result,
                           result_obj=result_obj,
                           user_name=user_name)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
