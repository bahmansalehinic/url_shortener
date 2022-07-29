from src.config import AppSettings, Config
from flask import Flask, request
from flask_cors import CORS, cross_origin
from src.application_service.exceptions import *
from src.application_service.ports.entry_point_service import *

app = Flask(__name__)

app.config.from_object(Config)
CORS(app)


@app.route('/url', methods=['POST'])
def shorten_url():
    try:
        long_url = request.json['long_url']
        print(request.json)
        print(long_url)
        data = create_shorten_url(long_url)
        return {'data': data}, 201
    except ApplicationError as err:
        return {'error': str(err)}, 400
    except Exception as err:
        return {'error': str(err)}, 500


if __name__ == '__main__':
    app.run(host=AppSettings.host, port=AppSettings.port)

