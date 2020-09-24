import requests
from flask import Blueprint, render_template, request

page = Blueprint('page', __name__)


@page.route('/health')
def healthy():
    r = requests.get(request.url_root)
    status = r.status_code
    message = r.reason
    return render_template('health.html', status=status, message=message)
