import bottle
import os
from bottle import route, run, view, template, static_file
from datetime import datetime

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
def about():
    """Страница 'О ферме'"""
    return template('about', 
                   title='О ферме',
                   year=datetime.now().year,
                   active_page='about')


@route('/jobs')
def jobs():
    """Страница 'Вакансии'"""
    return template('jobs', 
                   title='Вакансии',
                   year=datetime.now().year,
                   active_page='jobs')

@route('/contacts')
def contacts():
    """Страница 'Контакты'"""
    return template('contacts', 
                   title='Контакты',
                   year=datetime.now().year,
                   active_page='contacts')

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