#!/usr/bin/env python3
"""
Обертка для запуска приложения с обработкой ошибок версии системы.
Попробует найти рабочую версию Python и запустить приложение.
"""

import os
import sys
import subprocess

def find_python():
    """Находит доступные версии Python."""
    python_paths = [
        '/opt/homebrew/bin/python3.11',  # Homebrew Python 3.11 (приоритет)
        '/usr/local/bin/python3.11',
        '/opt/homebrew/bin/python3',
        '/usr/local/bin/python3',
        '/usr/bin/python3',
        'python3',
        'python'
    ]
    
    for path in python_paths:
        try:
            result = subprocess.run(
                [path, '--version'],
                capture_output=True,
                timeout=2
            )
            if result.returncode == 0:
                return path
        except:
            continue
    return None

def test_tkinter(python_path):
    """Проверяет, работает ли tkinter с данной версией Python."""
    try:
        result = subprocess.run(
            [python_path, '-c', 'import tkinter; tkinter._test()'],
            capture_output=True,
            timeout=3,
            env={**os.environ, 'TK_SILENCE_DEPRECATION': '1'}
        )
        return result.returncode == 0
    except:
        return False

def main():
    """Основная функция запуска."""
    print("Поиск рабочей версии Python...")
    
    python_path = find_python()
    if not python_path:
        print("Ошибка: Python не найден")
        sys.exit(1)
    
    print(f"Найден Python: {python_path}")
    
    # Пробуем запустить приложение
    script_dir = os.path.dirname(os.path.abspath(__file__))
    task_script = os.path.join(script_dir, 'task.py')
    
    env = os.environ.copy()
    env['TK_SILENCE_DEPRECATION'] = '1'
    env['PYTHONUNBUFFERED'] = '1'
    
    try:
        print("Запуск приложения...")
        subprocess.run([python_path, task_script], env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске: {e}")
        print("\nВозможные решения:")
        print("1. Установите Python через Homebrew: brew install python@3.11")
        print("2. Используйте IDE (VS Code, PyCharm) для запуска")
        print("3. Обновите систему до последней версии")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nПриложение прервано")
        sys.exit(0)

if __name__ == '__main__':
    main()

