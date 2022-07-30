from src.entry_point.flask_app import app
from src.config import AppSettings

if __name__ == '__main__':
    app.run(host=AppSettings.host, port=AppSettings.port)


