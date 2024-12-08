import json
import random
import time

def lambda_handler(event, context):
    MAX_RETRIES = 4
    RETRY_DELAY = 1

    try:
        # Parse the body to extract payment details
        body = json.loads(event.get('body', '{}'))
        payment_details = body.get('payment_details')

        if not payment_details:
            raise ValueError("Payment details are missing.")

        print(f"Processing payment: {payment_details}")

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                # Simulate a transient error with 30% probability
                if random.random() < 0.3:
                    raise Exception("TransientError")

                # Simulate successful payment processing
                print("Payment processed successfully.")
                return {
                    'statusCode': 200,
                    'body': json.dumps({
                        "message": "Payment processed successfully.",
                        "payment_details": payment_details
                    })
                }

            except Exception as e:
                if "TransientError" in str(e) and attempt < MAX_RETRIES:
                    print(f"Transient error occurred (attempt {attempt}/{MAX_RETRIES}). Retrying in {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                    RETRY_DELAY *= 2
                else:
                    raise e

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": "Payment processing failed.",
                "details": str(e)
            })
        }
