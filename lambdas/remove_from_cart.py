import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CartTable')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_id = body['userId']
        product_id = body['productId']

        table.delete_item(
            Key={
                'userId': user_id,
                'productId': product_id
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item removed from cart.'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
