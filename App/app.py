from flask import Flask, render_template, redirect

from Backend.building_result_list import add_to_list, delete_from_list, add_random_to_list

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


@app.route("/deleteResult/<user_name>")
def delete_result(user_name=None):
    delete_from_list(user_name, results_list)
    return redirect("/checkAccount")


@app.route("/randomAccount")
def random_account():
    add_random_to_list(results_list)
    return redirect("/checkAccount")


@app.route("/")
def main():
    return render_template("index.html", content=None)


if __name__ == '__main__':
    app.run()
