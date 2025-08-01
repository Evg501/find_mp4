import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from pack.file_lib import *

def find_mp4_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return []
    write_file( fname='last.html', text=response.text )
    soup = BeautifulSoup(response.text, 'html.parser')
    mp4_links = []

    # Находим все теги, у которых есть атрибут src
    for tag in soup.find_all(src=True):
        src = tag['src']
        link = urljoin(url, src)

        # Проверяем, заканчивается ли ссылка на .mp4 (регистронезависимо)
        if link.lower().endswith('.mp4'):
            mp4_links.append(link)

    # Убираем дубликаты
    mp4_links = list(set(mp4_links))

    return mp4_links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python find_mp4_links.py <URL>")
        sys.exit(1)

    page_url = sys.argv[1]
    links = find_mp4_links(page_url)

    if links:
        print("Найденные ссылки на .mp4 файлы:")
        for link in sorted(links):
            print(link)
    else:
        print("Ссылки на .mp4 файлы не найдены.")