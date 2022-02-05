
from flask import Flask, render_template, request
from subnet_calculation import *


app = Flask(__name__)


@app.route("/")
@app.route("/entry", methods=['GET', 'POST'])
def entry_page() -> 'html':

    return render_template('entry.html',
                           the_title='IP CALCULATOR')


@app.route("/result", methods=['POST'])
def calculate_res() -> 'html':

    title = "Here are your results"
    ip_address = request.form['ip_address']
    prefix = request.form['prefix']
    subnet = Subnet(ip_address, prefix)
    subnet.calculate()

    return render_template('results.html',
                           the_title=title,
                           the_ip_address=ip_address,
                           the_prefix=prefix,
                           the_network_id=subnet.SUBNET_INFO[subnet.address]["Network ID"],
                           the_net_cidr=subnet.SUBNET_INFO[subnet.address]["Netmask/CIDR"],
                           the_wildcard=subnet.SUBNET_INFO[subnet.address]["Wildcard"],
                           the_broadcast_ip=subnet.SUBNET_INFO[subnet.address]["Broadcast IP"],
                           the_first_ip=subnet.SUBNET_INFO[subnet.address]["First IP"],
                           the_last_ip=subnet.SUBNET_INFO[subnet.address]["Last IP"],
                           the_next_network=subnet.SUBNET_INFO[subnet.address]["Next Network ID"],
                           the_hosts=subnet.SUBNET_INFO[subnet.address]["Hosts"],)


if __name__ == '__main__':
    app.run(debug=True)
