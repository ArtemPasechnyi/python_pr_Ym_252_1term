# Программа для получения информации о репозитории GitHub
# Вариант 9: Automattic/wp-calypso
# Автор: pasechnyiad

import os
import sys
import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import urllib.request
import urllib.error
from typing import Optional, Dict, Any

# Устанавливаем переменные окружения ДО импорта tkinter
os.environ['TK_SILENCE_DEPRECATION'] = '1'


class GitHubAPI:
    """Класс для работы с GitHub API."""
    
    BASE_URL = "https://api.github.com"
    
    @staticmethod
    def get_repo_info(repo_name: str) -> Optional[Dict[str, Any]]:
        """
        Получает информацию о репозитории.
        
        Args:
            repo_name: Имя репозитория в формате 'owner/repo'
        
        Returns:
            Словарь с информацией о репозитории или None при ошибке
        """
        try:
            url = f"{GitHubAPI.BASE_URL}/repos/{repo_name}"
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Python-GitHub-API-Client')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise
        except Exception as e:
            raise
    
    @staticmethod
    def get_user_info(username: str) -> Optional[Dict[str, Any]]:
        """
        Получает информацию о пользователе/организации.
        
        Args:
            username: Имя пользователя или организации
        
        Returns:
            Словарь с информацией о пользователе или None при ошибке
        """
        try:
            url = f"{GitHubAPI.BASE_URL}/users/{username}"
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Python-GitHub-API-Client')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise
        except Exception as e:
            raise


class GitHubApp:
    """Главное приложение."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("GitHub Repository Info - pasechnyiad")
        self.root.geometry("700x600")
        
        # Основной фрейм
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Заголовок
        title_label = ttk.Label(
            main_frame,
            text="Получение информации о репозитории GitHub",
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=(0, 10))
        
        # Поле ввода
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Имя репозитория:").pack(side=tk.LEFT, padx=5)
        
        self.repo_entry = ttk.Entry(input_frame, width=40)
        self.repo_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.repo_entry.insert(0, "Automattic/wp-calypso")  # Значение по умолчанию для варианта 9
        
        # Кнопка получения данных
        self.fetch_button = ttk.Button(
            input_frame,
            text="Получить информацию",
            command=self.fetch_repo_info
        )
        self.fetch_button.pack(side=tk.LEFT, padx=5)
        
        # Область вывода результата
        ttk.Label(main_frame, text="Результат:").pack(anchor=tk.W, pady=(10, 5))
        
        self.result_text = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=("Courier", 10)
        )
        self.result_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Кнопка сохранения
        save_button = ttk.Button(
            main_frame,
            text="Сохранить в файл",
            command=self.save_to_file
        )
        save_button.pack(pady=5)
        
        self.current_data: Optional[Dict[str, Any]] = None
    
    def fetch_repo_info(self) -> None:
        """Получает информацию о репозитории."""
        repo_name = self.repo_entry.get().strip()
        
        if not repo_name:
            messagebox.showerror("Ошибка", "Введите имя репозитория!")
            return
        
        # Проверяем формат
        if '/' not in repo_name:
            messagebox.showerror("Ошибка", "Имя репозитория должно быть в формате 'owner/repo'")
            return
        
        self.fetch_button.config(state=tk.DISABLED)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Загрузка данных...\n")
        self.root.update()
        
        try:
            # Получаем информацию о репозитории
            repo_info = GitHubAPI.get_repo_info(repo_name)
            
            if repo_info is None:
                messagebox.showerror("Ошибка", f"Репозиторий '{repo_name}' не найден!")
                self.result_text.delete(1.0, tk.END)
                self.fetch_button.config(state=tk.NORMAL)
                return
            
            # Извлекаем имя владельца
            owner_name = repo_info.get('owner', {}).get('login', '')
            
            # Получаем информацию о пользователе/организации
            user_info = GitHubAPI.get_user_info(owner_name)
            
            if user_info is None:
                messagebox.showerror("Ошибка", f"Пользователь '{owner_name}' не найден!")
                self.result_text.delete(1.0, tk.END)
                self.fetch_button.config(state=tk.NORMAL)
                return
            
            # Формируем результат в нужном формате
            result = {
                'company': user_info.get('company'),
                'created_at': user_info.get('created_at'),
                'email': user_info.get('email'),
                'id': user_info.get('id'),
                'name': user_info.get('name') or user_info.get('login'),
                'url': user_info.get('url')
            }
            
            self.current_data = result
            
            # Выводим результат
            self.result_text.delete(1.0, tk.END)
            json_str = json.dumps(result, indent=2, ensure_ascii=False)
            self.result_text.insert(tk.END, json_str)
            
            messagebox.showinfo("Успех", "Информация успешно получена!")
        
        except urllib.error.URLError as e:
            messagebox.showerror("Ошибка сети", f"Не удалось подключиться к GitHub API:\n{e}")
            self.result_text.delete(1.0, tk.END)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")
            self.result_text.delete(1.0, tk.END)
        finally:
            self.fetch_button.config(state=tk.NORMAL)
    
    def save_to_file(self) -> None:
        """Сохраняет результат в JSON файл."""
        if self.current_data is None:
            messagebox.showwarning("Предупреждение", "Сначала получите информацию о репозитории!")
            return
        
        try:
            filename = "github_repo_info.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.current_data, f, indent=2, ensure_ascii=False)
            
            messagebox.showinfo("Успех", f"Данные сохранены в файл: {filename}")
        
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")


def main() -> None:
    """Точка входа в приложение."""
    try:
        root = tk.Tk()
        app = GitHubApp(root)
        root.mainloop()
    except tk.TclError as e:
        print(f"Ошибка Tkinter: {e}")
        print("Возможно, требуется обновление системы или Python")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nПриложение прервано")
        sys.exit(0)
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

