# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import bottle
import os
import json
from bottle import route, run, view, template, static_file, request, redirect
from datetime import datetime, timedelta

# Добавляем путь к папке static/JSON в sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'static', 'JSON'))

# Импортируем модуль novelties
import novelties


@route('/')
@view('layout')
def index():
    """Главная страница"""
    return{
        'title': 'Главная',
        'active_page': 'home',
        'year': datetime.now().year,
        'base': template('index')
        }

@route('/about')
@view('layout')
def about():
    return {
        'title': 'О ферме',
        'active_page': 'about',
        'year': 2026,
        'base': template('about')
    }

@route('/jobs')
@view('layout')
def jobs():
    return {
        'title': 'Вакансии',
        'active_page': 'jobs',
        'year': 2026,
        'base': template('jobs')
    }

@route('/contacts')
@view('layout')
def contacts():
    return {
        'title': 'Контакты',
        'active_page': 'contacts',
        'year': 2026,
        'base': template('contacts')
    }

@route('/novelties', method=['GET', 'POST'])
def novelties_page():
    """Страница новинок - возвращаем готовый HTML"""
    # Устанавливаем заголовок Content-Type
    bottle.response.content_type = 'text/html; charset=utf-8'
    errors = {}
    form_data = {}
    success_message = None
    
    # Загружаем список новинок
    novelties_list = novelties.load_novelties()
    
    # Вычисляем минимальную и максимальную дату для передачи в шаблон
    today = datetime.now().date()
    max_date = today + timedelta(days=5*365)  # +5 лет
    
    min_date_str = today.strftime('%Y-%m-%d')
    max_date_str = max_date.strftime('%Y-%m-%d')
    today_str = today.strftime('%d.%m.%Y')
    max_date_display = max_date.strftime('%d.%m.%Y')
    
    if request.method == 'POST':
        # Получаем данные из формы
        author = request.forms.get('author', '')
        title = request.forms.get('title', '')
        description = request.forms.get('description', '')
        date_str = request.forms.get('date', '')
        
        form_data = {
            'author': author,
            'title': title,
            'description': description,
            'date': date_str
        }
        
        # Валидация через функции из novelties.py
        is_valid, error = novelties.validate_author(author)
        if not is_valid:
            errors['author'] = error
        
        is_valid, error = novelties.validate_title(title)
        if not is_valid:
            errors['title'] = error
        
        is_valid, error = novelties.validate_description(description)
        if not is_valid:
            errors['description'] = error
        
        is_valid, error = novelties.validate_date(date_str)
        if not is_valid:
            errors['date'] = error
        
        # Если нет ошибок - сохраняем
        if not errors:
            result, error = novelties.add_novelty(author, title, description, date_str)
            if result:
                success_message = "Новинка успешно добавлена!"
                # Очищаем форму после успешной отправки
                form_data = {}
                # Перезагружаем список
                novelties_list = novelties.load_novelties()
            else:
                errors['general'] = error
    
    # Возвращаем готовый HTML шаблон (не через layout)
    return template('novelties', 
                   novelties=novelties_list, 
                   errors=errors, 
                   form_data=form_data,
                   success_message=success_message,
                   min_date=min_date_str,
                   max_date=max_date_str,
                   today_date=today_str,
                   max_date_display=max_date_display)

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        """Handler for static files, used with the development server.
        When running under a production server such as IIS or Apache,
        the server should be configured to serve the static files."""
        return bottle.static_file(filepath, root=STATIC_ROOT)

    bottle.run(server='wsgiref', host=HOST, port=PORT)