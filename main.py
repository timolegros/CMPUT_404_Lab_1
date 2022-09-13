import requests
from bs4 import BeautifulSoup

print(requests.__version__)

r = requests.get("https://www.google.com")

r2 = requests.get("https://github.com/timolegros/CMPUT_404_Lab_1/blob/main/main.py")
soup = BeautifulSoup(r2.text, 'html.parser')

table = soup.select('table[data-tagsearch-path="main.py"]')
items = table[0].select('td[class="blob-code blob-code-inner js-file-line"]')

print("\n\nSource code:\n")
for item in items:
    print(item.text)


