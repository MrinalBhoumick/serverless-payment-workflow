import json
import boto3
import uuid
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    try:
        # Generate a random payment ID using UUID
        payment_id = str(uuid.uuid4())

        # Retrieve status from the event
        status = event.get('status', 'Processed')

        # Update the order status in DynamoDB with the generated payment_ID
        response = table.update_item(
            Key={'PaymentId': payment_id},
            UpdateExpression='SET PaymentStatus = :val',
            ExpressionAttributeValues={':val': status}
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"Payment ID {payment_id} status updated to {status} successfully")
        }

    except ClientError as e:
        print(e.response['Error']['Message'])
        raise e

    except Exception as e:
        print(str(e))
        raise e
