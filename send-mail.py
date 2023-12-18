import requests
import os
from dotenv import load_dotenv

# Load variables from the "vars.env" file into the environment
load_dotenv(dotenv_path="vars.env")

# Elastic Email API key
api_key = os.environ.get("api_key")
print(api_key)

api_url = "https://api.elasticemail.com/v2/email/send"

# Email details
sender_email = "zachyrish@gmail.com"
recipient_email = "quanticrealm@gmail.com"
subject = "Test Email"
body = "Hello, this is a test email from Elastic Email API."

# Create the payload
payload = {
    "apikey": api_key,
    "from": sender_email,
    "to": recipient_email,
    "subject": subject,
    "bodyHtml": body,
}

try:
    res = requests.get(api_url)
    print(res)
    # Make a POST request to the Elastic Email API
    response = requests.post(api_url, data=payload)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print(response.status_code, response.text)
    # Check the response
    result = response.json()
    print(result)
    if result["success"]:
        print("Email sent successfully!")
    else:
        print(f"Failed to send email. Error: {result['error']}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
