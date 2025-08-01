import sys
import asyncio
from urllib.parse import urljoin
from playwright.async_api import async_playwright

async def find_mp4_links_with_playwright(url):
    mp4_links = []

    async with async_playwright() as p:
        try:
            # Запуск браузера (можно использовать 'chromium', 'firefox', 'webkit')
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            # Переход по URL
            await page.goto(url, wait_until="networkidle")  # ждём, пока страница "успокоится"

            # Получаем HTML после рендеринга JS
            content = await page.content()
            base_url = page.url  # на случай редиректа

            # Ищем все теги с атрибутом src
            elements = await page.query_selector_all('[src]')
            for elem in elements:
                src = await elem.get_attribute('src')
                if src and src.lower().endswith('.mp4'):
                    # Преобразуем в абсолютную ссылку
                    abs_link = urljoin(base_url, src)
                    mp4_links.append(abs_link)

            await browser.close()

        except Exception as e:
            print(f"Ошибка при обработке страницы: {e}")

    # Убираем дубликаты
    return list(set(mp4_links))

def main():
    if len(sys.argv) != 2:
        print("Использование: python find_mp4_links_playwright.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    print("Загружаем страницу и ищем .mp4 ссылки (с поддержкой JavaScript)...")
    links = asyncio.run(find_mp4_links_with_playwright(url))

    if links:
        print("Найденные ссылки на .mp4 файлы:")
        for link in sorted(links):
            print(link)
    else:
        print("Ссылки на .mp4 файлы не найдены.")

if __name__ == "__main__":
    main()