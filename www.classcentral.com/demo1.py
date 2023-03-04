import requests
import uuid
import json
from bs4 import BeautifulSoup
import datetime

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

# Load the HTML file
start = datetime.datetime.now()
with open('/Users/ihtre/OneDrive/Desktop/classCentral1/www.classcentral.com/report/feed/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all HTML tags that contain text and translate the text to Hindi
for element in soup.find_all(text=True):
    if element.parent.name in ['script', 'style']:
        continue
    text = element.strip()
    if text:
        # Define input text and request body
        body = [{
            "text": text
        }]

        # Send translation request
        response = requests.post(constructed_url, headers=headers, json=body)

        # Parse translation results
        results = response.json()
        translated_text = results[0]["translations"][0]["text"]

        # Replace original text with translated text
        element.replace_with(translated_text)

# Save the modified HTML to a file
with open('/Users/ihtre/OneDrive/Desktop/classCentral1/www.classcentral.com/report/feed/index_hi.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

end = datetime.datetime.now()
print(end-start)
