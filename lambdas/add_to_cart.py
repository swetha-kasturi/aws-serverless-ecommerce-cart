import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CartTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_id = body['userId']
        product_id = body['productId']
        quantity = body['quantity']
        added_at = datetime.now().isoformat()

        item = {
            'userId': user_id,
            'productId': product_id,
            'quantity': quantity,
            'addedAt': added_at
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item added to cart!', 'item': item})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
