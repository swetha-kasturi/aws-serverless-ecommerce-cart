import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CartTable')  # Use your actual table name

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        user_id = body['userId']
        product_id = body['productId']
        new_quantity = body['quantity']

        response = table.update_item(
            Key={
                'userId': user_id,
                'productId': product_id
            },
            UpdateExpression='SET quantity = :q',
            ExpressionAttributeValues={
                ':q': new_quantity
            }
        )

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Quantity updated successfully.'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
