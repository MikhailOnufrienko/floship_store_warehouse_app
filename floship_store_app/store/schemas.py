from pydantic import BaseModel


class UserAuthenticationRequest(BaseModel):
    username: str
    password: str
