const apiUrl = 'https://7eewqf6u00.execute-api.ap-south-1.amazonaws.com/Prod/startPayment';

document.getElementById('start_payment_button').addEventListener('click', startPayment);

function startPayment() {
    const card_number = document.getElementById('card_number').value;
    const expiry_date = document.getElementById('expiry_date').value;
    const cvv = document.getElementById('cvv').value;
    const amount = document.getElementById('amount').value;

    if (!card_number || !expiry_date || !cvv || !amount) {
        displayMessage('Please fill out all the fields.', 'error');
        return;
    }

    const paymentDetails = {
        payment_details: {
            card_number,
            expiry_date,
            cvv,
            amount: parseFloat(amount)
        }
    };

    const requestPayload = JSON.stringify(paymentDetails);

    // Disable button to prevent multiple submissions
    const button = document.getElementById('start_payment_button');
    button.disabled = true;
    displayMessage('Processing payment...', 'info');

    fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: requestPayload
    })
    .then(response => response.json())
    .then(data => {
        if (data.statusCode === 200) {
            displayMessage('Payment processing started successfully. Check your email for updates!', 'success');
        } else {
            displayMessage('There was an error with the payment processing.', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        displayMessage('Error occurred during payment processing. Please try again later.', 'error');
    })
    .finally(() => {
        // Re-enable button
        button.disabled = false;
    });
}

function displayMessage(message, type) {
    const responseMessageElement = document.getElementById('response_message');
    responseMessageElement.style.display = 'block';
    responseMessageElement.className = `response ${type}`;
    responseMessageElement.textContent = message;
}
