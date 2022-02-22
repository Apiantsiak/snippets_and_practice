

from flask import Flask, render_template, request, session

from subnet_calculation import Subnet
from DB_context_mng import UseDataBase
from checker import check_logged_in


app = Flask(__name__)

app.config["dbconfig"] = {"host": "127.0.0.1",
                          "user": "avp",
                          "password": "153624",
                          "database": "subnet_logDB",
                          }


@app.route("/login")
def do_log_in() -> str:
    session["logged_in"] = True
    return "You are now logged in."


@app.route("/logout")
def do_log_out() -> str:
    session.pop("logged_in")
    return "You are now logged out."


@app.route("/")
@app.route("/entry", methods=["GET", "POST"])
def entry_page() -> "html":

    return render_template("entry.html",
                           the_title="IP CALCULATOR",
                           )


def log_request(req: "flask_request", res: str) -> None:

    with UseDataBase(app.config["dbconfig"]) as cursor:

        _SQL = """insert into log
                  (user_data, results, ip_addr, browser_str)
                  values
                  (%s, %s, %s, %s);"""

        form_items = ", ".join([f"{key}:{val}" for key, val in req.form.items()])

        cursor.execute(_SQL, (form_items,
                              res,
                              req.user_agent.browser,
                              req.remote_addr,
                              )
                       )


@app.route("/result", methods=["POST"])
def calculate_res() -> "html":

    title = "Here are your results"
    ip_address = request.form["ip_address"]
    prefix = request.form["prefix"]
    subnet = Subnet(ip_address, prefix)
    subnet.calculate()
    result = subnet.SUBNET_INFO[subnet.address].items()
    log_request(request, "; ".join(subnet.SUBNET_INFO[subnet.address].values()))

    return render_template("results.html",
                           the_title=title,
                           the_ip_address=ip_address,
                           the_prefix=prefix,
                           the_data=result,
                           )


@app.route("/viewlog", methods=["GET", "POST"])
@check_logged_in
def view_the_log() -> "html":

    with UseDataBase(app.config["dbconfig"]) as cursor:
        _SQL = """select * from log;"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ("Id", "Time", "Form Data", "Results", "User_agent", "Remote_addr")

    return render_template("viewlog.html",
                           the_title="View Log",
                           the_row_titles=titles,
                           the_data=contents,
                           )


app.secret_key = "MayTheForceBeWithYou"

if __name__ == '__main__':
    app.run(debug=True)
