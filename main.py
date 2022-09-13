import requests

print(requests.__version__)

r = requests.get("https://www.google.com")

r = requests.get("https://github.com/timolegros/CMPUT_404_Lab_1/blob/main/main.py")
