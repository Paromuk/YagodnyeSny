# -*- coding: utf-8 -*-
import json
import os
import re
from datetime import datetime

# Путь к файлу с данными (в корне проекта)
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'novelties.json')


def validate_author(author):
    """Валидация автора: буквы, цифры (до 4), пробелы, только . знак"""
    if not author or len(author.strip()) < 2:
        return False, "Author name must contain at least 2 characters"
    if len(author.strip()) > 50:
        return False, "Author name must not exceed 50 characters"
    
    # Подсчитываем количество цифр
    digit_count = sum(1 for char in author if char.isdigit())
    if digit_count > 4:
        return False, "Author name can contain no more than 4 digits"
    
    # Разрешены: буквы, цифры, пробелы, точка (.)
    pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9\s\.]+$'
    if not re.match(pattern, author.strip()):
        return False, "Author name can only contain letters, digits (max 4), spaces and dots (.)"
    
    # Запрещаем спецсимволы подряд
    if re.search(r'[^a-zA-Zа-яА-ЯёЁ0-9\s\.]', author):
        return False, "Author name cannot contain special characters like @#$%^&*()"
    
    return True, ""


def validate_title(title):
    """Валидация названия: буквы, цифры, пробелы, знаки . , ! ?"""
    if not title or len(title.strip()) < 3:
        return False, "Title must contain at least 3 characters"
    if len(title.strip()) > 100:
        return False, "Title must not exceed 100 characters"
    
    # Проверка, что название не состоит только из цифр
    if re.match(r'^\d+$', title.strip()):
        return False, "Title cannot consist only of digits"
    
    # Запрещаем недопустимые символы (разрешены: буквы, цифры, пробелы, . , ! ?)
    if re.search(r'[^a-zA-Zа-яА-ЯёЁ0-9\s\.\,\!\\?]', title):
        return False, "Title can only contain letters, digits, spaces and punctuation (. , ! ?)"
    
    # Запрещаем повторяющиеся спецсимволы подряд (например: !! ,,, ...)
    if re.search(r'([\.\,\!\\?])\1{2,}', title):
        return False, "Title cannot have repeating punctuation marks (e.g., ... ,,, !!!)"
    
    return True, ""


def validate_description(description):
    """Валидация описания: буквы, цифры, пробелы, знаки . , ! ? и перенос строки"""
    if not description or len(description.strip()) < 10:
        return False, "Description must contain at least 10 characters"
    if len(description.strip()) > 500:
        return False, "Description must not exceed 500 characters"
    
    # Проверка, что описание не состоит только из цифр и пробелов
    if re.match(r'^[\d\s\.\,\!\\?]+$', description.strip()):
        return False, "Description cannot consist only of digits and punctuation"
    
    # Разрешены: буквы, цифры, пробелы, . , ! ? и перенос строки
    if re.search(r'[^a-zA-Zа-яА-ЯёЁ0-9\s\.\,\!\\?\n]', description):
        return False, "Description can only contain letters, digits, spaces, punctuation (. , ! ?) and line breaks"
    
    # Запрещаем повторяющиеся спецсимволы подряд (например: ..... ,,,, !!!)
    if re.search(r'([\.\,\!\\?])\1{2,}', description):
        return False, "Description cannot have repeating punctuation marks (e.g., ... ,,, !!!)"
    
    return True, ""


def validate_date(date_str):
    """Валидация даты: не может быть меньше текущей и больше текущей даты"""
    if not date_str:
        return False, "Date field is required"
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        
        if date_obj < current_date:
            return False, f"Date cannot be earlier than today ({current_date.strftime('%d.%m.%Y')})"
        
        max_future_date = current_date.replace(year=current_date.year + 5)
        if date_obj > max_future_date:
            return False, f"Date cannot be later than 5 years from now ({max_future_date.strftime('%d.%m.%Y')})"
        
        return True, ""
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD"


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
            
            # Сортировка: сначала по дате (новые сверху), затем по ID (новые сверху)
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
        print(f"Error saving: {e}")


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
    
    novelties_list = load_novelties()
    new_id = max([n.get('id', 0) for n in novelties_list], default=0) + 1
    
    novelty = {
        'id': new_id,
        'author': author.strip(),
        'title': title.strip(),
        'description': description.strip(),
        'date_added': date_added,
        'created_at': datetime.now().isoformat()
    }
    
    novelties_list.append(novelty)
    novelties_list.sort(key=lambda x: (x.get('date_added', ''), x.get('id', 0)), reverse=True)
    save_novelties(novelties_list)
    
    return novelty, None
