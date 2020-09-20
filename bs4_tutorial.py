import requests
from bs4 import BeautifulSoup

def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title_tag = soup.find('body').find('h1')
    link_image = soup.find('body').find('div', class_='bookimage').find('img')['src']
    post_text = soup.find('body').find_all('table', class_='d_book')[1].text
    title_author = title_tag.find('a').text
    title_text = title_tag.text.split('\xa0 :: \xa0')[0].strip(' ')
    return title_text, link_image, post_text, title_author

if __name__ == "__main__":
    print(get_title(url))