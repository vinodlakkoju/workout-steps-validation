import json
from DetectionEngine import DetectEngine

def lambda_handler(event, context):
    user_id = event["queryStringParameters"]["user_id"]
    score_date = event["queryStringParameters"]["current_date"]
    print(user_id, score_date)
    de = DetectEngine(int(user_id), score_date)
    result, reason = de.isValidScore()

    return {
        'statusCode': 200,
        'body': json.dumps(str({'result': result, 'reason': reason}))
    }
