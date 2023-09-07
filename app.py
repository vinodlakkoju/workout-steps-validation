from fastapi import FastAPI
import uvicorn
import json
from DetectionEngine import DetectEngine


WEB_IP_ADR = '0.0.0.0'
app = FastAPI()

@app.get('/healthcheck')
def healthCheck() -> str:
    return 'I am okay'

@app.get('/detectfraud/{user_id}/{score_date}')
def detectFraud(user_id, score_date) -> str:
    de = DetectEngine(int(user_id), score_date)
    result, reason = de.isValidScore()
    # return json.dumps({'result': result, 'reason': reason})
    return str({'result': result, 'reason': reason})


def runService() -> None:
    """
    Entry-level for the service invocation
    :return: None
    """
    app.debug = True
    # uvicorn.run(app, host=WEB_IP_ADR, port=9090)
    uvicorn.run(app, port=8080)


if __name__ == '__main__':
    try:
        runService()
    except Exception as ex:
        print(f'Abort: {ex}')