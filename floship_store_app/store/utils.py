import requests

from .schemas import UserAuthenticationRequest
from floship_store_app.config import project_settings 


csrf_token: str | None = None


def get_csrf_token() -> str:
    response = requests.get('http://127.0.0.1:8002/admin/')
    global csrf_token
    csrf_token = response.cookies.get('csrftoken')
    return csrf_token


def authenticate_user(user: UserAuthenticationRequest, csrf_token: str) -> None:
    requests.post(
        'http://127.0.0.1:8002/admin/login/',
        data={'username': user.username, 'password': user.password},
        cookies={'csrftoken': csrf_token},
        headers={'X-CSRFToken': csrf_token, 'Content-type': 'application/json'}
    )

def get_user() -> UserAuthenticationRequest:
    return UserAuthenticationRequest(
        username=project_settings.WAREHOUSE_USERNAME,
        password=project_settings.WAREHOUSE_PASSWORD
)