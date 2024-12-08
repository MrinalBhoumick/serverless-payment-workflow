import json

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # Validate the payment details from the event
    payment_details = event.get('payment_details')
    if not payment_details:
        raise ValueError("Missing payment details.")

    print("Payment Details:", payment_details)

    if not validate_payment(payment_details):
        raise Exception("Invalid Payment Details")

    # Return payment details along with success message
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Payment validation successful, Workflow initiated.',
            'payment_details': payment_details
        })
    }

def validate_payment(details):
    # Add payment validation logic here
    if not details.get('card_number') or not details.get('expiry_date') or not details.get('cvv'):
        return False
    return True
