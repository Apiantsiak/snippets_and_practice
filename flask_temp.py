from flask import Flask
from func_temp import network_id


app = Flask(__name__)


@app.route("/")
def take_ip() -> str:
    return "Enter ip"


@app.route("/network_id")
def show_network() -> str:
    return network_id("127.0.0.1", "24")


app.run()
