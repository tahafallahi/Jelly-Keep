import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0',}

def get_page_url(word):
    params = {'q':word}
    url = requests.get('https://www.oxfordlearnersdictionaries.com/search/english/', params=params, headers=headers).request.url
    if 'spellcheck' in url:
        return False
    else:
        return url

def get_mp3(page_url):
    response = requests.get(page_url, headers=headers) 
    soup = BeautifulSoup(response.text, 'lxml')
    cookedsoup = soup.find('div', class_='sound audio_play_button pron-us icon-audio')['data-src-mp3']
    return cookedsoup
