from flask import Flask, render_template, flash

app = Flask(__name__)


def check_button_click():
    print("ok")


@app.route("/checkAccount")
def check_account():
    return render_template("checkAccount.html", content=None)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
