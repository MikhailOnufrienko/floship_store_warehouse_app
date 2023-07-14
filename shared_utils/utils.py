import requests

from .schemas import UserAuthenticationRequest
from project_config import project_settings


csrf_token: str | None = None


def get_csrf_token(app_port: str) -> str:
    response = requests.get(f'http://127.0.0.1:{app_port}/admin/')
    global csrf_token
    csrf_token = response.cookies.get('csrftoken')
    return csrf_token


def authenticate_user(
        user: UserAuthenticationRequest,
        csrf_token: str,
        app_port: str) -> None:
    requests.post(
        f'http://127.0.0.1:{app_port}/admin/login/',
        data={'username': user.username, 'password': user.password},
        cookies={'csrftoken': csrf_token},
        headers={'X-CSRFToken': csrf_token, 'Content-type': 'application/json'}
    )

def get_user(app_name: str) -> UserAuthenticationRequest:
    if app_name == project_settings.WAREHOUSE_APP_NAME:
        return UserAuthenticationRequest(
            username=project_settings.STORE_ADMIN_USERNAME,
            password=project_settings.STORE_ADMIN_PASSWORD
    )
    return UserAuthenticationRequest(
        username=project_settings.WAREHOUSE_ADMIN_USERNAME,
        password=project_settings.WAREHOUSE_ADMIN_PASSWORD
    )
