import requests
import uuid
import json

# Define endpoint and API parameters
endpoint = "https://keerthi771.cognitiveservices.azure.com/"
path = "/translator/text/v3.0/translate?api-version=3.0"
params = "&to=hi"
constructed_url = endpoint + path + params

# Define subscription key and headers
subscription_key = "17fb8cb26be44cf7a4cb32861bb2c542"
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4())
}

# Define input text and request body
input_text = "Hello, how are you?"
body = [{
    "text": input_text
}]

# Send translation request
response = requests.post(constructed_url, headers=headers, json=body)

# Print translation results
results = response.json()
print(json.dumps(results, indent=4, ensure_ascii=False))
