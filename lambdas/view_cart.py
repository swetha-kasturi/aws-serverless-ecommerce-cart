import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CartTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_id = body['userId']

        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('userId').eq(user_id)
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'items': response.get('Items', [])})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
