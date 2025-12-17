# Приложение с графическим интерфейсом
# Автор: pasechnyiad

import os
import sys

# Устанавливаем переменные окружения ДО импорта tkinter
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Пробуем импортировать tkinter
try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog, scrolledtext
except ImportError as e:
    print(f"Ошибка импорта tkinter: {e}")
    print("Убедитесь, что tkinter установлен")
    sys.exit(1)


class CalculatorTab:
    """Вкладка с простым калькулятором."""
    
    def __init__(self, parent: ttk.Frame):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Первое число
        ttk.Label(self.frame, text="Первое число:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.num1_entry = ttk.Entry(self.frame, width=20)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Операция
        ttk.Label(self.frame, text="Операция:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.operation_var = tk.StringVar(value="+")
        operation_combo = ttk.Combobox(
            self.frame,
            textvariable=self.operation_var,
            values=["+", "-", "*", "/"],
            state="readonly",
            width=17
        )
        operation_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Второе число
        ttk.Label(self.frame, text="Второе число:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.num2_entry = ttk.Entry(self.frame, width=20)
        self.num2_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Кнопка вычисления
        calc_button = ttk.Button(self.frame, text="Вычислить", command=self.calculate)
        calc_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        
        # Результат
        ttk.Label(self.frame, text="Результат:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.result_label = ttk.Label(self.frame, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
    
    def calculate(self) -> None:
        """Выполняет вычисление."""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль невозможно!")
                    return
                result = num1 / num2
            else:
                return
            
            self.result_label.config(text=f"{result:.2f}")
        
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


class CheckboxTab:
    """Вкладка с чекбоксами."""
    
    def __init__(self, parent: ttk.Frame):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Чекбоксы
        self.checkbox1_var = tk.BooleanVar()
        self.checkbox2_var = tk.BooleanVar()
        self.checkbox3_var = tk.BooleanVar()
        
        checkbox1 = ttk.Checkbutton(
            self.frame,
            text="Первый",
            variable=self.checkbox1_var
        )
        checkbox1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        
        checkbox2 = ttk.Checkbutton(
            self.frame,
            text="Второй",
            variable=self.checkbox2_var
        )
        checkbox2.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        
        checkbox3 = ttk.Checkbutton(
            self.frame,
            text="Третий",
            variable=self.checkbox3_var
        )
        checkbox3.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        
        # Кнопка
        button = ttk.Button(self.frame, text="Показать выбор", command=self.show_selection)
        button.grid(row=3, column=0, padx=10, pady=20)
    
    def show_selection(self) -> None:
        """Показывает всплывающее окно с выбранными вариантами."""
        selected = []
        
        if self.checkbox1_var.get():
            selected.append("первый")
        if self.checkbox2_var.get():
            selected.append("второй")
        if self.checkbox3_var.get():
            selected.append("третий")
        
        if selected:
            message = f"Вы выбрали: {', '.join(selected)} вариант(ы)."
        else:
            message = "Вы не выбрали ни одного варианта."
        
        messagebox.showinfo("Выбор", message)


class TextTab:
    """Вкладка для работы с текстом."""
    
    def __init__(self, parent: ttk.Frame, root: tk.Tk):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.root = root
        
        # Текстовое поле
        ttk.Label(self.frame, text="Текст:").pack(anchor=tk.W, pady=(0, 5))
        
        self.text_area = scrolledtext.ScrolledText(
            self.frame,
            wrap=tk.WORD,
            width=50,
            height=15
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def load_from_file(self) -> None:
        """Загружает текст из файла."""
        filename = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
                messagebox.showinfo("Успех", "Файл успешно загружен!")
            
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")


class MainApplication:
    """Главное приложение."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("pasechnyiad")
        self.root.geometry("600x500")
        
        # Создаем вкладки
        notebook = ttk.Notebook(root, padding="10")
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Первая вкладка - калькулятор
        calc_frame = ttk.Frame(notebook)
        notebook.add(calc_frame, text="Калькулятор")
        CalculatorTab(calc_frame)
        
        # Вторая вкладка - чекбоксы
        checkbox_frame = ttk.Frame(notebook)
        notebook.add(checkbox_frame, text="Чекбоксы")
        CheckboxTab(checkbox_frame)
        
        # Третья вкладка - текст
        text_frame = ttk.Frame(notebook)
        notebook.add(text_frame, text="Текст")
        self.text_tab = TextTab(text_frame, root)
        
        # Создаем меню после инициализации всех вкладок
        menubar = tk.Menu(root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Загрузить из файла", command=self.load_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=root.destroy)
        
        menubar.add_cascade(label="Файл", menu=file_menu)
        root.config(menu=menubar)
    
    def load_file(self) -> None:
        """Загружает файл в текстовую вкладку."""
        if hasattr(self, 'text_tab'):
            self.text_tab.load_from_file()


def main() -> None:
    """Точка входа в приложение."""
    try:
        # Попытка создать окно с обработкой ошибок версии
        try:
            root = tk.Tk()
        except Exception as init_error:
            # Если ошибка связана с версией, пробуем обходной путь
            error_str = str(init_error)
            if "macOS" in error_str or "required" in error_str:
                print("Обнаружена проблема с версией системы.")
                print("Попытка запуска с обходным путем...")
                # Пробуем установить переменные окружения и перезапустить
                os.environ['TK_SILENCE_DEPRECATION'] = '1'
                # Пробуем еще раз
                try:
                    root = tk.Tk()
                except:
                    print("Не удалось запустить приложение из-за проблем с системой.")
                    print("Попробуйте:")
                    print("1. Обновить Python до последней версии")
                    print("2. Использовать другую версию Python")
                    print("3. Запустить через IDE (VS Code, PyCharm)")
                    sys.exit(1)
            else:
                raise
        
        app = MainApplication(root)
        root.mainloop()
    except tk.TclError as e:
        print(f"Ошибка Tkinter: {e}")
        print("Возможно, требуется обновление системы или Python")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nПриложение прервано пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

