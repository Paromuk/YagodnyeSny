# -*- coding: utf-8 -*-
import bottle
import os
import sys
from bottle import route, run, view, template, static_file, request
from datetime import datetime, timedelta

# ПРЯМОЙ импорт novelties (без добавления пути)
# Так как novelties.py в папке static/JSON, нужно указать полный путь
import importlib.util

# Загружаем novelties из папки static/JSON
spec = importlib.util.spec_from_file_location(
    "novelties", 
    os.path.join(os.path.dirname(__file__), 'static', 'JSON', 'novelties.py')
)
novelties = importlib.util.module_from_spec(spec)
spec.loader.exec_module(novelties)


@route('/')
@view('layout')
def index():
    return {
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
        'year': datetime.now().year,
        'base': template('about')
    }

@route('/jobs')
@view('layout')
def jobs():
    return {
        'title': 'Вакансии',
        'active_page': 'jobs',
        'year': datetime.now().year,
        'base': template('jobs')
    }

@route('/contacts')
@view('layout')
def contacts():
    return {
        'title': 'Контакты',
        'active_page': 'contacts',
        'year': datetime.now().year,
        'base': template('contacts')
    }

@route('/novelties', method=['GET', 'POST'])
@view('layout')
def novelties_page():
    errors = {}
    form_data = {}
    success_message = None
    
    today = datetime.now().date()
    max_date = today + timedelta(days=5*365)
    
    novelties_list = novelties.load_novelties()
    
    if request.method == 'POST':
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
        
        valid, err = novelties.validate_author(author)
        if not valid: errors['author'] = err
        
        valid, err = novelties.validate_title(title)
        if not valid: errors['title'] = err
        
        valid, err = novelties.validate_description(description)
        if not valid: errors['description'] = err
        
        valid, err = novelties.validate_date(date_str)
        if not valid: errors['date'] = err
        
        if not errors:
            result, err = novelties.add_novelty(author, title, description, date_str)
            if result:
                success_message = "Novelty successfully added!"
                form_data = {}
                novelties_list = novelties.load_novelties()
            else:
                errors['general'] = err
    
    return {
        'title': 'Novelties',
        'active_page': 'novelties',
        'year': datetime.now().year,
        'base': template('novelties', 
                       novelties=novelties_list,
                       errors=errors,
                       form_data=form_data,
                       success_message=success_message,
                       min_date=today.strftime('%Y-%m-%d'),
                       max_date=max_date.strftime('%Y-%m-%d'),
                       today_date=today.strftime('%d.%m.%Y'),
                       max_date_display=max_date.strftime('%d.%m.%Y'))
    }

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 5555
    bottle.run(server='wsgiref', host=HOST, port=PORT, debug=True)