import json
import os
import re
from datetime import datetime

DATA_FILE = 'partners.json'

def load_partners():
    """Загрузка списка партнёров из JSON-файла"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_partners(partners):
    """Сохранение списка партнёров в JSON-файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(partners, f, ensure_ascii=False, indent=4)

def validate_phone(phone):
    """Проверка формата номера телефона с помощью регулярного выражения"""
    pattern = r'^\+7\d{10}$'
    return re.match(pattern, phone) is not None

def validate_date(date_str):
    """Проверка корректности даты в формате ГГГГ-ММ-ДД"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_partner(author, description, phone, date):
    """Добавление нового партнёра в список"""
    partners = load_partners()
    new_id = max([p['id'] for p in partners], default=0) + 1 #генерация нового id
    new_partner = {
        'id': new_id,
        'author': author.strip(),
        'description': description.strip(),
        'phone': phone.strip(),
        'date': date.strip()
    }
    partners.insert(0, new_partner) #новые записи - в начало списка
    save_partners(partners)
    return new_partner