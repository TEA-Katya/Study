import tkinter as tk
from tkinter import messagebox
import json
import requests

def get_repo_data():
    repo_name = entry.get().strip()
    if not repo_name:
        messagebox.showerror("Ошибка", "Введите имя репозитория (в виде: владелец/репозиторий)")
        return

    url = f"https://api.github.com/repos/{repo_name}"

    try:
        headers = {"User-Agent": "GitHubRepoInfoFetcher/1.0 (Python Tkinter)"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        #Выбираем нужные поля
        fields_to_extract = ['id', 'name', 'created_at']
        selected_data = {field: data.get(field) for field in fields_to_extract}

        #Обрабатываем 'url', чтобы получить HTML-ссылку
        selected_data['url'] = data.get('html_url')

        #Добавляем 'company' и 'email' 
        selected_data['company'] = data.get('company')
        selected_data['email'] = data.get('email')

        filename = f"{repo_name.replace('/', '_')}_info.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(selected_data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("Успех", f"Данные репозитория сохранены в файл {filename}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка запроса", f"Не удалось получить данные: {e}\nВозможно, репозиторий не существует или проблемы с сетью.")
    except json.JSONDecodeError as e:
        messagebox.showerror("Ошибка JSON", f"Не удалось обработать ответ от сервера: {e}")
    except Exception as e:
        messagebox.showerror("Общая ошибка", f"Произошла непредвиденная ошибка: {e}")

root = tk.Tk()
root.title("GitHub Repo Info")

tk.Label(root, text="Введите имя репозитория (owner/repo, например, dotnet/runtime):").pack(padx=10, pady=5)
entry = tk.Entry(root, width=50)
entry.insert(0, "dotnet/corefx")
entry.pack(padx=10, pady=5)
btn = tk.Button(root, text="Получить данные", command=get_repo_data)
btn.pack(padx=10, pady=10)

root.mainloop()
