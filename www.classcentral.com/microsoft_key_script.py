import requests
from bs4 import BeautifulSoup

# Load the HTML file
with open('/Users/ihtre/OneDrive/Desktop/classCentral1/www.classcentral.com/university/edinburgh.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all HTML tags that contain text and translate the text to Hindi
subscription_key = '17fb8cb26be44cf7a4cb32861bb2c542'
endpoint = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=hi'
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-type': 'application/json'}

for element in soup.find_all(text=True):
    if element.parent.name in ['script', 'style']:
        continue
    text = element.strip()
    if text:
        try:
            body = [{'text': text}]
            response = requests.post(endpoint, headers=headers, json=body)
            response.raise_for_status()
            translated_text = response.json()[0]['translations'][0]['text']
            element.replace_with(translated_text)
        except requests.exceptions.HTTPError as error:
            print(f'HTTP error occurred: {error}')
            print(f'Response content: {response.content}')
        except Exception as error:
            print(f'Error occurred: {error}')

# Save the modified HTML to a file
with open('edinburgh_hi.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
