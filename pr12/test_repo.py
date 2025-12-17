#!/usr/bin/env python3
"""
Тестовый скрипт для получения информации о репозитории Automattic/wp-calypso
и сохранения в файл.
"""

import json
import urllib.request
import urllib.error

def get_repo_info(repo_name: str):
    """Получает информацию о репозитории."""
    url = f"https://api.github.com/repos/{repo_name}"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Python-GitHub-API-Client')
    
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())

def get_user_info(username: str):
    """Получает информацию о пользователе/организации."""
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Python-GitHub-API-Client')
    
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())

def main():
    repo_name = "Automattic/wp-calypso"
    
    print(f"Получение информации о репозитории: {repo_name}")
    
    try:
        # Получаем информацию о репозитории
        repo_info = get_repo_info(repo_name)
        owner_name = repo_info.get('owner', {}).get('login', '')
        
        print(f"Владелец репозитория: {owner_name}")
        
        # Получаем информацию о владельце
        user_info = get_user_info(owner_name)
        
        # Формируем результат
        result = {
            'company': user_info.get('company'),
            'created_at': user_info.get('created_at'),
            'email': user_info.get('email'),
            'id': user_info.get('id'),
            'name': user_info.get('name') or user_info.get('login'),
            'url': user_info.get('url')
        }
        
        # Выводим результат
        print("\nРезультат:")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        
        # Сохраняем в файл
        filename = "github_repo_info.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\nДанные сохранены в файл: {filename}")
        
    except urllib.error.URLError as e:
        print(f"Ошибка сети: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

