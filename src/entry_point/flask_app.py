from src.config import AppSettings, Config
from flask import Flask, request, jsonify, redirect
from src.application_service.ports.entry_point_service import *
from src.entry_point.utils import is_from_browser
from src.application_service.decorators import url_error_handler
import webbrowser

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/url', methods=['POST'], endpoint='shorten_url')
@url_error_handler
def shorten_url():
    long_url = request.json['url']
    data = create_shorten_url(long_url)
    return jsonify(data), 201


@app.route('/url', methods=['PUT'], endpoint='update_url')
@url_error_handler
def update_url():
    long_url = request.json['url']
    new_long_url = request.json['new_url']
    data = modify(long_url, new_long_url)
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
        #return jsonify(f'a web browser is opened for {data}'), 200


@app.route('/url', methods=['DELETE'], endpoint='delete_url')
@url_error_handler
def delete_url():
    url = request.json['url']
    data = delete(url)
    return jsonify(data), 204


if __name__ == '__main__':
    app.run(host=AppSettings.host, port=AppSettings.port)

