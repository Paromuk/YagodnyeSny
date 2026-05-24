import bottle
import os
from bottle import route, run, view, template, static_file, request, redirect
from partners_manager import load_partners, add_partner, validate_phone, validate_date
from datetime import datetime
import re

bottle.BaseRequest.MAX_BODY_SIZE = 10485760
request.charset = 'utf-8'
bottle.TEMPLATE_SETTINGS = {'doctype': 'HTML5', 'encoding': 'utf-8'}

@route('/')
@view('layout')
def index():
    """Главная страница"""
    return{
        'title': 'Главная',
        'active_page': 'home',
        'year':datetime.now().year,
        'base':template('index')
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

@route('/partners')
@view('layout')
def partners():
    partners_list = load_partners()
    return {
        'title': 'Партнёры',
        'active_page': 'partners',
        'year': 2026,
        'base': template('partners', 
                       partners_list=partners_list,
                       author='',
                       description='',
                       phone='',
                       date='',
                       error=None,
                       success=None,
                       field_errors={})
    }

# Обработчик формы партнёров (POST)
@route('/add_partner', method='POST')
def add_partner_handler():
    """Обработка формы добавления партнёра"""
    from urllib.parse import unquote, parse_qs
    
    # Получаем сырое тело запроса и декодируем правильно
    raw_data = request.body.read().decode('utf-8')
    
    # Парсим вручную URL-encoded данные
    parsed = parse_qs(raw_data)
    
    author = parsed.get('author', [''])[0].strip()
    description = parsed.get('description', [''])[0].strip()
    phone = parsed.get('phone', [''])[0].strip()
    date = parsed.get('date', [''])[0].strip()
    
    field_errors = {}
    
    # валидация: наименование компании
    if not author:
        field_errors['author'] = 'Поле обязательно для заполнения'
    elif len(author) < 2:
        field_errors['author'] = 'Название компании должно содержать не менее 2 символов'
    elif len(author) > 100:
        field_errors['author'] = 'Название компании не должно превышать 100 символов'
    elif not re.match(r'^[a-zA-Zа-яА-ЯёЁ0-9\s\-\.,"]+$|^$', author):
        field_errors['author'] = 'Название компании содержит недопустимые символы'
    
    # валидация: описание
    if not description:
        field_errors['description'] = 'Поле обязательно для заполнения'
    elif len(description) < 5:
        field_errors['description'] = 'Описание должно содержать не менее 5 символов'
    elif len(description) > 1000:
        field_errors['description'] = 'Описание не должно превышать 1000 символов'
    
    # валидация: телефон
    if not phone:
        field_errors['phone'] = 'Поле обязательно для заполнения'
    elif not validate_phone(phone):
        field_errors['phone'] = 'Телефон должен быть в формате +71234567890 (11 цифр)'
    
    # валидация: дата
    if not date:
        field_errors['date'] = 'Поле обязательно для заполнения'
    elif not validate_date(date):
        field_errors['date'] = 'Дата должна быть в формате ГГГГ-ММ-ДД'
    else:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.now().date()
        if input_date > today:
            field_errors['date'] = 'Дата не может быть в будущем'
    
    partners_list = load_partners()
    
    if field_errors:
        content = template('partners', 
                          partners_list=partners_list,
                          author=author,
                          description=description,
                          phone=phone,
                          date=date,
                          error="Пожалуйста, исправьте ошибки в форме",
                          success=None,
                          field_errors=field_errors)
        return template('layout',
                       title='Партнёры',
                       active_page='partners',
                       year=2026,
                       base=content)

    add_partner(author, description, phone, date)
    partners_list = load_partners()
    content = template('partners', 
                      partners_list=partners_list,
                      author='',
                      description='',
                      phone='',
                      date='',
                      error=None,
                      success="Партнёр успешно добавлен!",
                      field_errors={})
    return template('layout',
                   title='Партнёры',
                   active_page='partners',
                   year=2026,
                   base=content)

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
        return bottle.static_file(filepath, root=STATIC_ROOT)

    bottle.run(server='wsgiref', host=HOST, port=PORT)