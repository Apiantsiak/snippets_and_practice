

from threading import Thread
from flask import Flask, render_template, request, session, copy_current_request_context

from subnet_calculation import Subnet
from DB_context_mng import UseDataBase, DBConnectionError, CredentialsError, SQLError
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
def entry_page():
    """Display webapp's HTML form

    :return: html
    """
    return render_template("entry.html",
                           the_title="IP CALCULATOR",
                           )


@app.route("/result", methods=["POST"])
def calculate_res():
    """Extract the posted data; perform the calculation; return results

    :return: html
    """

    @copy_current_request_context
    def log_request(req, res: str) -> None:
        """Log details of the web request and the results

        :param req: flask_request
        :param res: str
        :return: None
        """
        try:
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
        except DBConnectionError as error:
            print(f"Database connection failed. Error :  {str(error)}")
        except CredentialsError as error:
            print(f"User-id/Password issues. Error: {str(error)}")
        except SQLError as error:
            print(f"Incorrect query. Error: {str(error)}")
        except Exception as error:
            print(f"Something went wrong: {str(error)}")

    title = "Here are your results"
    ip_address = request.form["ip_address"]
    prefix = request.form["prefix"]

    try:
        subnet = Subnet(ip_address, prefix)
        subnet.calculate()
        result = subnet.SUBNET_INFO[subnet.address].items()
        rez = "; ".join(subnet.SUBNET_INFO[subnet.address].values())
    except Exception as err:
        print(f"Empty input: Error {str(err)}")
        return render_template("entry.html",
                               the_title="IP CALCULATOR",
                               the_err_mes="Please enter correct values"
                               )
    try:
        thread = Thread(target=log_request, args=(request, rez))
        thread.start()
    except Exception as err:
        print(f"Logging failed with this error: {str(err)}")
    return render_template("results.html",
                           the_title=title,
                           the_ip_address=ip_address,
                           the_prefix=prefix,
                           the_data=result,
                           )


@app.route("/viewlog", methods=["GET", "POST"])
@check_logged_in
def view_the_log():
    """Display the contents of the log table from subnet_logDB database as HTML table

    :return: html
    """
    try:
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
    except DBConnectionError as err:
        print(f"Database connection failed. Error :  {str(err)}")
        return render_template("entry.html",
                               the_title="IP CALCULATOR",
                               )
    except CredentialsError as err:
        print(f"User-id/Password issues. Error: {str(err)}")
        return render_template("entry.html",
                               the_title="IP CALCULATOR",
                               )
    except SQLError as err:
        print(f"Is your query correct? Error: {str(err)}")
        return render_template("entry.html",
                               the_title="IP CALCULATOR",
                               )
    except Exception as err:
        print(f"Something went wrong: {str(err)}")
        return render_template("entry.html",
                               the_title="IP CALCULATOR",
                               )


app.secret_key = "MayTheForceBeWithYou"

if __name__ == '__main__':
    app.run(debug=True)
