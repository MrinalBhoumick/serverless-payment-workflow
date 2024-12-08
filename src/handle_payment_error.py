import json

def lambda_handler(event, context):
    try:
        # Log the error and perform error handling
        print("Handling payment error for event:", event)

        # Simulate error handling logic
        return {
            'statusCode': 200,
            'body': json.dumps("Payment error handled successfully")

        }
    except Exception e:
        print(str(e))
        raise e