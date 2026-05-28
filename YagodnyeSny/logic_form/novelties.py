import json
import os
import re
from datetime import datetime

# Путь к файлу с данными (в корне проекта)
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'novelties.json')


def validate_author(author):
    """Валидация автора: буквы, цифры (до 4), пробелы, максимум 1 точка"""
    if not author or len(author.strip()) < 2:
        return False, "Имя автора должно содержать не менее 2 символов"
    if len(author.strip()) > 50:
        return False, "Имя автора не должно превышать 50 символов"
    
    digit_count = sum(1 for char in author if char.isdigit())
    if digit_count > 4:
        return False, "Имя автора может содержать не более 4 цифр"
    
    dot_count = author.count('.')
    if dot_count > 1:
        return False, "Имя автора может содержать не более одной точки (.)"
    
    pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9\s\.]+$'
    if not re.match(pattern, author.strip()):
        return False, "Имя автора может содержать только буквы, цифры (не более 4), пробелы и точку (.)"
    
    return True, ""


def validate_title(title):
    """Валидация названия: буквы, цифры, пробелы, знаки . , ! ?"""
    if not title or len(title.strip()) < 3:
        return False, "Название должно содержать не менее 3 символов"
    if len(title.strip()) > 100:
        return False, "Название не должно превышать 100 символов"
    
    if re.match(r'^\d+$', title.strip()):
        return False, "Название не может состоять только из цифр"
    
    if re.search(r'[^a-zA-Zа-яА-ЯёЁ0-9\s\.\,\!\\?]', title):
        return False, "Название может содержать только буквы, цифры, пробелы и знаки препинания (. , ! ?)"
    
    if re.search(r'([\.\,\!\\?])\1{2,}', title):
        return False, "Название не может содержать повторяющиеся знаки препинания (например: ... ,,, !!!)"
    
    return True, ""


def validate_description(description):
    """Валидация описания: буквы, цифры, пробелы, знаки . , ! ? и перенос строки"""
    if not description or len(description.strip()) < 10:
        return False, "Описание должно содержать не менее 10 символов"
    if len(description.strip()) > 500:
        return False, "Описание не должно превышать 500 символов"
    
    if re.match(r'^[\d\s\.\,\!\\?]+$', description.strip()):
        return False, "Описание не может состоять только из цифр и знаков препинания"
    
    if re.search(r'[^a-zA-Zа-яА-ЯёЁ0-9\s\.\,\!\\?\n]', description):
        return False, "Описание может содержать только буквы, цифры, пробелы, знаки препинания (. , ! ?) и переносы строк"
    
    if re.search(r'([\.\,\!\\?])\1{2,}', description):
        return False, "Описание не может содержать повторяющиеся знаки препинания (например: ... ,,, !!!)"
    
    return True, ""


def validate_date(date_str):
    """Валидация даты: не может быть раньше сегодняшнего дня и не позже чем через 5 лет"""
    if not date_str:
        return False, "Поле 'Дата' обязательно для заполнения"
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        
        if date_obj < current_date:
            return False, f"Дата не может быть раньше сегодняшнего дня ({current_date.strftime('%d.%m.%Y')})"
        
        max_future_date = current_date.replace(year=current_date.year + 5)
        if date_obj > max_future_date:
            return False, f"Дата не может быть позже чем через 5 лет ({max_future_date.strftime('%d.%m.%Y')})"
        
        return True, ""
    except ValueError:
        return False, "Неверный формат даты. Используйте ГГГГ-ММ-ДД"


def check_duplicate(author, title, description):
    """Проверка на дубликаты"""
    novelties_list = load_novelties()
    
    for item in novelties_list:
        if (item.get('author', '').lower() == author.lower() and
            item.get('title', '').lower() == title.lower() and
            item.get('description', '').lower() == description.lower()):
            return False, "Такая новинка уже существует! Вы не можете добавить точно такую же запись."
    
    return True, ""


def load_novelties():
    """Загрузка списка новинок из JSON файла с сортировкой"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                if 'date_added' in item and item['date_added']:
                    try:
                        date_obj = datetime.strptime(item['date_added'], '%Y-%m-%d')
                        item['date_formatted'] = date_obj.strftime('%d.%m.%Y')
                    except:
                        item['date_formatted'] = item['date_added']
            
            data.sort(key=lambda x: (x.get('date_added', ''), x.get('id', 0)), reverse=True)
            return data
    except (json.JSONDecodeError, IOError):
        return []


def save_novelties(novelties_list):
    """Сохранение списка новинок в JSON файл"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(novelties_list, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка сохранения: {e}")


def add_novelty(author, title, description, date_added):
    """Добавление новой новинки с валидацией"""
    is_valid, error = validate_author(author)
    if not is_valid:
        return None, error
    
    is_valid, error = validate_title(title)
    if not is_valid:
        return None, error
    
    is_valid, error = validate_description(description)
    if not is_valid:
        return None, error
    
    is_valid, error = validate_date(date_added)
    if not is_valid:
        return None, error
    
    is_valid, error = check_duplicate(author, title, description)
    if not is_valid:
        return None, error
    
    novelties_list = load_novelties()
    new_id = max([n.get('id', 0) for n in novelties_list], default=0) + 1
    
    novelty = {
        'id': new_id,
        'author': author.strip(),
        'title': title.strip(),
        'description': description.strip(),
        'date_added': date_added
    }
    
    novelties_list.append(novelty)
    novelties_list.sort(key=lambda x: (x.get('date_added', ''), x.get('id', 0)), reverse=True)
    save_novelties(novelties_list)
    
    return novelty, "Новинка успешно добавлена!"