import os
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import re

# # Define the URL of Google Translate
# url = 'https://translate.google.com/m'

# # Define the target language
# target_lang = 'hi'

# Loop through all the HTML files in a directory
for filename in os.listdir('/Users/ihtre/OneDrive/Desktop/classCentral1/www.classcentral.com'):
    if filename.endswith('.html'):
        filepath = os.path.join('/Users/ihtre/OneDrive/Desktop/classCentral1/www.classcentral.com', filename)
        
        # Read the contents of the HTML file
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            print("reading file")

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find all the text nodes in the HTML
        html_tags = soup.find_all(text=True)

        # Find all HTML tags that contain text and translate the text to Hindi
        translator = Translator()
        translator.raise_Exception = True
        
        # Loop through each text node and translate the text
        for tag in html_tags:
            # Send the text to Google Translate
            if tag.parent.name in ['div', 'span', 'h1', 'h2', 'h3', 'p', 'button', 'a']:
                text = re.sub(r'\s+', ' ', tag.string.strip())
                if text:
                    translated_text = translator.translate(tag, dest='hi').text
                    tag.replace_with(translated_text)
                else:
                    pass
            # tag.replace_with(translated_text)
            # params = {'hl': 'en', 'sl': 'auto', 'tl': target_lang, 'q': node}
            # response = requests.get(url, params=params)
            
            # # Parse the response using BeautifulSoup
            # translated_node = BeautifulSoup(response.text, 'html.parser').find('span', {'class': 'tlid-translation translation'})
            
            # # Replace the original text with the translated text
            # node.replace_with(translated_node.text)
        
        # Write the translated HTML back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            print("write file")