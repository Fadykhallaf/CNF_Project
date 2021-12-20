from flask import Flask, Response, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/status')
def status():
    res = {'result': 'OK - healthy'}
    response = app.response_class(response=json.dumps(res),
     status=200, 
     mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
