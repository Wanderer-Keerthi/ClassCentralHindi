from googletrans import Translator
from bs4 import BeautifulSoup
import re
# import time
import datetime

# Load the HTML file
start = datetime.datetime.now()
with open('/Users/ihtre/OneDrive/Desktop/classCentral1/www.classcentral.com/university/edinburgh.html', 'r', encoding='utf-8') as f:
    html = f.read()


# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all HTML tags that contain text and translate the text to Hindi
translator = Translator(service_urls=['translate.google.com'])
count = 0

for element in soup.find_all(text=True):
    if element.parent.name in ['script', 'style']:
        continue
    text = element.strip()
    if text:
        try:
            translated_text = translator.translate(text, src='en', dest='hi').text
            element.replace_with(translated_text)
        except:
            pass
# for tag in soup.find_all(text=True):
#     if tag.parent.name in ['div', 'span', 'h1', 'h2', 'h3', 'p', 'button', 'a']:
#         text = re.sub(r'\s+', ' ', tag.string.strip())
#         print(text)
#         if text:
#             count += 1
#             translated_text = translator.translate(tag, dest='hi').text
#             # print(translated_text)
#             tag.replace_with(translated_text)
#             print(count)
#             # time.sleep(0.3)

# Save the modified HTML to a file
with open('edinburgh_hi.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

end = datetime.datetime.now()
print(end-start)


# translator = Translator(service_urls=['translate.google.com'])

# for element in text_elements:
#     if element.parent.name in ['script', 'style']:
#         continue
#     text = element.strip()
#     if text:
#         try:
#             translated_text = translator.translate(text, src='en', dest='hi').text
#             element.replace_with(translated_text)
#         except:
#             pass

# translated_html_content = str(soup)
# with open('translated_page.html', 'w', encoding='utf-8') as f:
#     f.write(translated_html_content)
