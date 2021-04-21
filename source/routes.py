import requests
from sanic import Blueprint

page = Blueprint('page', __name__)


@page.route('/')
def healthy():
    return 'HELLOW'
    # r = requests.get(request.base_url)
    # status = r.status_code
    # message = r.reason
    # return render_template('health.html', status=status, message=message)


def send_message():
    print('Hellow World')