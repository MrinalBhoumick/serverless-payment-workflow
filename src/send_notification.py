import json
import boto3
from botocore.exceptions import ClientError

sns_client = boto3.client('sns')
topic_arn = 'arn:aws:sns:ap-south-1:418272791444:OrderNotifications'

def lambda_handler(event, context):
    try:
        # Retrieve order ID and status from the event
        order_id = event.get('order_id')
        status = event.get('status', 'Processed')

        # Create the message to send
        message = f"Order {order_id} status has been updated to {status}."

        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Order Status Update"
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"Notification sent for order {order_id}")
        }

    except ClientError as e:
        print(e.response['Error']['Message'])
        raise e

    except Exception as e:
        print(str(e))
        raise e
