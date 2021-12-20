import logging
from flask import Flask, Response, json
app = Flask(__name__)

@app.route("/")
def hello():
    logging.debug('Home page url')
    return "Hello World!"

@app.route('/status')
def status():
    response = app.response_class(json.dumps({'result': 'OK - healthy'}),
     status=200, 
     mimetype='application/json')
    logging.debug('status endpoint was reached')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
     status=200, 
     mimetype='application/json')
    logging.debug("metrics endpoint was reached")
    return response


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
