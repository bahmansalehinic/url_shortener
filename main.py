from src.config import AppSettings, Config
from flask import Flask, request, jsonify, redirect
from src.application_service.ports.entry_point_service import *
from src.entry_point.utils import is_from_browser
from src.application_service.ports.decorators import url_error_handler

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/url', methods=['POST'], endpoint='shorten_url')
@url_error_handler
def shorten_url():
    long_url = request.json['long_url']
    data = create_shorten_url(long_url)
    return jsonify(data), 201


@app.route('/url/<path:url>', methods=['GET'], endpoint='get_url')
@url_error_handler
def get_url(url):
    data = find_url(url)
    return jsonify(data), 200


@app.route('/<path:url>', methods=['GET'], endpoint='visit_url')
@url_error_handler
def visit_url(url):
    data = visit(url)
    if is_from_browser(request.user_agent):
        return redirect(data, 302)
    else:
        return webbrowser.open(data)


if __name__ == '__main__':
    app.run(host=AppSettings.host, port=AppSettings.port)

