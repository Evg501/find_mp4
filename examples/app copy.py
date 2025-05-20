
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def find_mp4_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    mp4_links = []

    for a_tag in soup.find_all('a', href=True):
        link = urljoin(url, a_tag['href'])
        if link.lower().endswith('.mp4'):
            mp4_links.append(link)

    return mp4_links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python find_mp4_links.py <URL>")
        sys.exit(1)

    page_url = sys.argv[1]
    links = find_mp4_links(page_url)

    if links:
        print("Найденные ссылки на .mp4 файлы:")
        for link in links:
            print(link)
    else:
        print("Ссылки на .mp4 файлы не найдены.")
        
#<a href="https://vestivrn.ru/media/archive/video/2025/05/Owlczn-6Tn3XVbQeMwxhJHrV6b12gE9H.mp4" download>Скачать PDF</a>  


