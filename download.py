import requests

def download_book(url, filename):
    responce = requests.get(url)
    responce.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(responce.content)