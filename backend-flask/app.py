import os

# from flask_restful import Api, Resource
import sys
import threading
from crypt import methods
from time import sleep

from flask import Flask, render_template

app = Flask(__name__)
# api = Api (app)


def _get_data() -> dict:
    data_dict = {
        "China": "1,412,600,000",
        "India": "1,407,563,842",
        "USA": "332,951,233",
        "Indonesia": "272,248,500",
        "Pakistan": "235,824,862",
    }
    return data_dict


@app.route("/")
def index():
    return render_template("index.html")


# api.add_resource(Data, "/data")

# methods not necessarily needed
@app.route("/data", methods=["POST", "GET"])
def data():
    return _get_data()


@app.route("/liveness")
def liveness():
    # sleep(2)
    return "<h1><center>Liveness check completed</center><h1>"


@app.route("/readiness")
def readiness():
    sleep(20)
    return "<h1><center>Readiness check completed</center><h1>"


def _thread_kill_in_seconds(KILL_IN_SECONDS: int):
    if KILL_IN_SECONDS is not None:
        print("kill active")
        for i in range(KILL_IN_SECONDS):
            sleep(1)
            if i % 5 == 0:
                print(f"shutdown in {KILL_IN_SECONDS-i}")
            if i == KILL_IN_SECONDS - 3:
                print(f"shutdown in 3")
            if i == KILL_IN_SECONDS - 2:
                print(f"shutdown in 2")
            if i == KILL_IN_SECONDS - 1:
                print(f"shutdown in 1")
        os._exit(0)


if __name__ == "__main__":
    KILL_IN_SECONDS = os.environ.get("KILL_IN_SECONDS")
    KILL_IN_SECONDS = int(KILL_IN_SECONDS)
    t1 = threading.Thread(target=_thread_kill_in_seconds, args=(KILL_IN_SECONDS,))
    t1.start()

    app.run(debug=True, host="0.0.0.0", port="5000")
