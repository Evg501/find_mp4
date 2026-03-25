import tkinter as tk
from tkinter import scrolledtext
import re
import requests
from urllib.parse import urljoin, urlparse


def find_mp4_links(url):
    """
    Функция для поиска ссылок на MP4-файлы на веб‑странице.
    Возвращает список найденных URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Регулярное выражение для поиска MP4‑ссылок
        mp4_pattern = r'https?://[^\s"\'<>`]+\.mp4'
        found_links = re.findall(mp4_pattern, response.text)
        
        # Убираем дубликаты и сортируем
        unique_links = sorted(set(found_links))
        return unique_links
    
    except requests.RequestException as e:
        return [f"Ошибка при запросе: {e}"]
    except Exception as e:
        return [f"Неожиданная ошибка: {e}"]

def on_button_click():
    """Обработчик нажатия кнопки 'Запуск'."""
    url = entry_url.get().strip()
    
    if not url:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Пожалуйста, введите URL")
        return
    
    # Очищаем поле вывода
    output_text.delete(1.0, tk.END)
    
    # Показываем статус обработки
    output_text.insert(tk.END, "Поиск MP4‑ссылок...\n\n")
    root.update()  # Обновляем интерфейс
    
    # Вызываем функцию поиска и получаем результат
    links = find_mp4_links(url)
    
    # Отображаем результат
    output_text.delete(1.0, tk.END)
    if links:
        for link in links:
            output_text.insert(tk.END, link + "\n")
    else:
        output_text.insert(tk.END, "MP4‑ссылки не найдены")

# Создаём главное окно
root = tk.Tk()
root.title("Поиск MP4‑ссылок")
root.geometry("700x500")
root.resizable(True, True)

# Фрейм для URL‑поля и кнопки
input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

# Метка для поля ввода URL
label_url = tk.Label(input_frame, text="Введите URL:")
label_url.pack(anchor=tk.W)

# Поле ввода URL
entry_url = tk.Entry(input_frame, width=80, font=("Arial", 10))
entry_url.pack(fill=tk.X, pady=5)

# Привязываем стандартные сочетания клавиш
entry_url.bind('<Control-c>', lambda event: root.focus_get().event_generate('<<Copy>>'))
#entry_url.bind('<Control-v>', lambda event: root.focus_get().event_generate('<<Paste>>'))
entry_url.bind('<Control-x>', lambda event: root.focus_get().event_generate('<<Cut>>'))
entry_url.bind('<Control-a>', lambda event: root.focus_get().select_range(0, tk.END))

# Создаём и привязываем контекстное меню
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Вырезать", command=lambda: entry_url.event_generate('<<Cut>>'))
context_menu.add_command(label="Копировать", command=lambda: entry_url.event_generate('<<Copy>>'))
context_menu.add_command(label="Вставить", command=lambda: entry_url.event_generate('<<Paste>>'))
context_menu.add_separator()
context_menu.add_command(label="Выделить всё", command=lambda: entry_url.select_range(0, tk.END))

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

entry_url.bind("<Button-3>", show_context_menu)

# Кнопка «Запуск»
button_run = tk.Button(input_frame, text="Запуск", command=on_button_click, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
button_run.pack(pady=5)

# Фрейм для поля вывода
output_frame = tk.Frame(root)
output_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Метка для поля вывода
label_output = tk.Label(output_frame, text="Найденные MP4‑ссылки:")
label_output.pack(anchor=tk.W)

# Многострочное поле вывода с прокруткой
output_text = scrolledtext.ScrolledText(
    output_frame,
    wrap=tk.WORD,
    width=80,
    height=20,
    font=("Arial", 9)
)
output_text.pack(fill=tk.BOTH, expand=True)

# Запускаем главный цикл приложения
root.mainloop()
