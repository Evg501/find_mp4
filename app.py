import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from pack.file_lib import *
from rich import print
from rich.console import Console

DOWNLOAD_DIR = 'downloads'

def find_mp4_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    mp4_links = []

    # Ищем все теги <source>, у которых атрибут src заканчивается на .mp4
    for source_tag in soup.find_all('source', src=True):
        link = urljoin(url, source_tag['src'])
        if link.lower().endswith('.mp4'):
            mp4_links.append(link)

    return mp4_links

if __name__ == "__main__":
    #if len(sys.argv) != 2:
    #    print("Использование: python find_mp4_links.py <URL>")
    #    sys.exit(1)
    print('[grey37]hello', '[red]hello')
    set_this_dir()
    #curr_dir = get_curr_dir(__file__) + '\\' + DOWNLOAD_DIR
    curr_dir = get_exe_dir(arg1=__file__) + '\\' + DOWNLOAD_DIR
    print('[orange4]папка: ', '[orange4]'+curr_dir )
    print()
    #exit()
    mkdir_if_no_exist(curr_dir)
    #page_url = sys.argv[1]
    while True:
        print("[green3]Введите url")
        page_url = input()
        
        links = find_mp4_links(page_url)

        if links:
            print("Найденные ссылки на .mp4 файлы:")
            for link in links:
                print(link)
                fname = os.path.basename(link)
                full_name = os.path.join(curr_dir, fname)
                if not os.path.exists(full_name):
                    print("Скачивание...")
                    download_file(urlfile=link, path=curr_dir, check_exist=True)
                else:
                    print('[red]file exists: ' + fname )
        else:
            print("Ссылки на .mp4 файлы не найдены.")