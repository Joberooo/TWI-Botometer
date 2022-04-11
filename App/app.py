import botometer
from flask import Flask, render_template
from result import Result

from Backend import apiBotometer

app = Flask(__name__)


@app.route("/checkAccount")
def check_accountOne():
    return render_template("checkAccount.html", result=None)


@app.route("/checkAccount/<user_name>")
def check_accountTwo(user_name=None):
    if user_name is not None:
        try:
            result_obj = Result(apiBotometer.check_account(user_name))
        except botometer.NoTimelineError:
            result_obj = Result("hasNoTimeline")
        except botometer.TweepError:
            result_obj = Result("doesntExist")
    else:
        result_obj = None
    return render_template("checkAccount.html",
                           result_obj=result_obj,
                           user_name=user_name)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
