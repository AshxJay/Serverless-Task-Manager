import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON"})
        }

    title = body.get("title")

    if not title or not isinstance(title, str):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Title is required and must be a string"})
        }

    task_id = str(uuid.uuid4())

    item = {
        "taskId": task_id,
        "title": title,
        "status": "TODO",
        "createdAt": datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Task created",
            "taskId": task_id
        })
    }
