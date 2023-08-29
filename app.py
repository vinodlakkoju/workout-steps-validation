import flask
from flask import Flask
from flask_cors import CORS
import json
import os
from time import time
from DetectionEngine import DetectEngine



WEB_IP_ADR = '0.0.0.0'
app = Flask(__name__)
CORS(app)

@app.route('/healthcheck', methods=['GET'])
def healthCheck() -> str:
    return 'I am okay'

@app.route('/detectfraud/<user_id>/<score_date>', methods=['GET'])
def detectFraud(user_id, score_date) -> str:
    de = DetectEngine()
    result, reason = de.isValidScore(int(user_id), score_date)
    return json.dumps({'result': result, 'reason': reason})


def runService() -> None:
    """
    Entry-level for the service invocation
    :return: None
    """
    app.debug = True
    app.run(host=WEB_IP_ADR, port=9090, processes=True)


if __name__ == '__main__':
    try:
        runService()
    except Exception as ex:
        print(f'Abort: {ex}')