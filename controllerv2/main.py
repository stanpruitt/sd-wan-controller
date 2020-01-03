from controllerv2.core import Singleton

from flask import render_template
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
@app.route("/index.htm")
def index():
    region = "Baicells"
    fatedges = [
        {
            'Name': 'Beijing',
            'SN': 'Unknown',
            'IP': 'Unknown',
            'NetworkModel': 'Unknown',
            'Online': 'OFF',
            'SPEC': 'Unknown',
            'SW': 'Unknown',
            'ThinEdges': [
                {
                    'Name': 'Nanjing',
                    'SN': 'Unknown',
                    'IP': 'Unknown',
                    'Online': 'OFF',
                    'SPEC': 'Unknown',
                    'SW': 'Unknown',
                    'Tunnels': 'Unknown'
                },
                {
                    'Name': 'Shenzhen',
                    'SN': 'Unknown',
                    'IP': 'Unknown',
                    'Online': 'OFF',
                    'SPEC': 'Unknown',
                    'SW': 'Unknown',
                    'Tunnels': 'Unknown'
                },
                {
                    'Name': 'AliCloud',
                    'SN': 'Unknown',
                    'IP': 'Unknown',
                    'Online': 'OFF',
                    'SPEC': 'Unknown',
                    'SW': 'Unknown',
                    'Tunnels': 'Unknown'
                },
            ]
        },
    ]
    return render_template("overview.html", region=region, fatedges=fatedges)

@app.route("/todo")
@app.route("/todo/")
def todo():
    return render_template("todo.html")

@app.route("/north/", methods=("POST", ))
def north():
    cmd = request.form["CMD"]
    if cmd == "poll":
        SN = request.form["SN"]
        return Singleton.getInstance().getresponse(SN)
    elif cmd == "query":
        return "Query OK"
    else:
        return "Unknown"


if __name__ == "__main__":
    app.run()

