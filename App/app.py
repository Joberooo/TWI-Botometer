from flask import Flask, render_template
from Backend.building_result_list import add_to_list

app = Flask(__name__)
results_list = []


@app.route("/checkAccount")
def check_accountOne():
    return render_template("checkAccount.html", results_list=results_list)


@app.route("/checkAccount/<user_name>")
def check_accountTwo(user_name=None):
    add_to_list(user_name, results_list)
    return render_template("checkAccount.html",
                           results_list=results_list,
                           user_name=user_name)


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
