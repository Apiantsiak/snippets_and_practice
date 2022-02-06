
from flask import Flask, render_template, request, escape
from subnet_calculation import *


app = Flask(__name__)


@app.route("/")
@app.route("/entry", methods=["GET", "POST"])
def entry_page() -> "html":

    return render_template("entry.html",
                           the_title="IP CALCULATOR")


def log_request(req: "flask_request", res: str) -> None:
    with open("sub_app_log.txt", "a") as log:
        form_items = ", ".join([f"{key}:{val}" for key, val in req.form.items()])
        print(form_items, res, req.user_agent, req.remote_addr, file=log, sep="|")


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
                           the_data=result,)


@app.route("/viewlog", methods=["GET", "POST"])
def view_the_log() -> "html":

    contents = []
    with open("sub_app_log.txt") as log:
        log_ls = log.readlines()
        for pos, line in enumerate(log_ls):
            contents.append([str(pos + 1)])
            for item in line.split("|"):
                contents[pos].append(escape(item))

    titles = ("№", "Form Data", "Results", "User_agent", "Remote_addr")

    return render_template("viewlog.html",
                           the_title="View Log",
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
