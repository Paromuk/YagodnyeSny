import bottle
from bottle import route, run, template, static_file

# Маршруты для страниц
@route('/')
def index():
    """Главная страница"""
    return template('index')

@route('/about')
def about():
    """Страница 'О ферме'"""
    return template('about')

@route('/jobs')
def jobs():
    """Страница 'Вакансии'"""
    return template('jobs')

@route('/contacts')
def contacts():
    """Страница 'Контакты'"""
    return template('contacts')

#Маршрут для статических файлов
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

#Запуск сервера
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)