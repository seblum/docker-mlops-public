from crypt import methods
import os
from flask import Flask, render_template
from time import sleep
#from flask_restful import Api, Resource
import sys

app = Flask(__name__)
#api = Api (app)

KILL_IN_SECONDS = os.environ.get("KILL_IN_SECONDS")

if KILL_IN_SECONDS is not None:
    print("in loop")
    sleep(int(KILL_IN_SECONDS))
    sys.exit()
# class Data(Resource):
#     def get(self):
#         return _get_data

def _get_data() -> dict:
    data_dict = {'China': '1,412,600,000',
    'India': '1,407,563,842',
    'USA': '332,951,233',
    'Indonesia' : '272,248,500',
    'Pakistan' : '235,824,862'
    }
    return data_dict

@app.route('/')
def index():
    return render_template('index.html')

#api.add_resource(Data, "/data")

# methods not necessarily needed
@app.route('/data', methods = ["POST","GET"])
def data():
    return _get_data()

@app.route('/liveness')
def liveness():
    #sleep(2)
    return "<h1><center>Liveness check completed</center><h1>"

@app.route('/readiness')
def readiness():
    #sleep(20)
    return "<h1><center>Readiness check completed</center><h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')