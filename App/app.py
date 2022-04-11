from flask import Flask, render_template, flash

from Backend import apiBotometer

app = Flask(__name__)


@app.route("/checkAccount")
def check_accountOne():
    return render_template("checkAccount.html", result=None)


@app.route("/checkAccount/<user_name>")
def check_accountTwo(user_name=None):
    if user_name is not None:
        result = apiBotometer.check_account(user_name)
    else:
        result = None
    return render_template("checkAccount.html", result=result, user_name=user_name)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
