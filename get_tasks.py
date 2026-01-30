import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    limit = int(params.get("limit", 5))
    last_key = params.get("lastKey")

    scan_kwargs = {
        "Limit": limit
    }

    if last_key:
        scan_kwargs["ExclusiveStartKey"] = {"taskId": last_key}

    response = table.scan(**scan_kwargs)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "items": response.get("Items", []),
            "nextKey": response.get("LastEvaluatedKey", {}).get("taskId")
        })
    }
