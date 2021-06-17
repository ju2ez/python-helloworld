from flask import Flask
from flask import json
import logging



app = Flask(__name__)
logging.basicConfig(filename='app.log',
                            filemode='a',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    logging.info("status")
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    logging.info('Metrics')
    return response

@app.route("/")
def hello():
    logging.info('Hello')
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
