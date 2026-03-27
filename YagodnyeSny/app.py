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