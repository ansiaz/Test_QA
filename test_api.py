import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv(override=True)

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

BASE_URL = 'https://api.github.com'

def create_repo():
    url = f'{BASE_URL}/user/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': REPO_NAME,
        'private': False  # Публичный репозиторий
    }
    print(GITHUB_TOKEN)
    response = requests.post(url, headers=headers, json=data)
    return response

def repo_exists():
    url = f'{BASE_URL}/users/{GITHUB_USERNAME}/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    repos = response.json()
    return any(repo['name'] == REPO_NAME for repo in repos)

def delete_repo():
    url = f'{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.delete(url, headers=headers)
    return response

if __name__ == '__main__':
    # Создание репозитория
    create_response = create_repo()
    if create_response.status_code == 201:
        print(f'Repository "{REPO_NAME}" created successfully.')
        
        # Проверка существования репозитория
        if repo_exists():
            print(f'Repository "{REPO_NAME}" exists.')
            
            # Удаление репозитория
            delete_response = delete_repo()
            if delete_response.status_code == 204:
                print(f'Repository "{REPO_NAME}" deleted successfully.')
            else:
                print(f'Failed to delete repository: {delete_response.status_code}')
        else:
            print(f'Repository "{REPO_NAME}" does not exist.')
    else:
        print(f'Failed to create repository: {create_response.status_code}')
