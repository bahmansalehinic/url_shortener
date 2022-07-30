from src.application_service.exceptions import ApplicationError


def url_error_handler(func):

    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except ApplicationError as err:
            return {'error': str(err)}, 400
        except Exception as err:
            return {'error': str(err)}, 500
    return wrapper
