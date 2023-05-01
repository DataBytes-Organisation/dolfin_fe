from app import cache
from classes.api import API
from dash import html
import dash_core_components as dcc
from utils.constants import login_location
from typing import Union, Any

class Auth:
    def __init__(self) -> None:
        pass

    def is_authenticated() -> bool:
        try:
            email = cache.get("email")
            tokens = cache.get("tokens")
            if email is None: raise Exception("email not in cache")
            if tokens is None: raise Exception("tokens not in cache")
            api = API()
            api.refresh_token_auth(email=email, tokens=tokens) 
            return True
        except Exception as e:
            return False

    def set_cache(email: str, tokens: dict):
        try:
            cache.set("email", email)
            cache.set("tokens", tokens)
            cached_email, cached_token = cache.get("email"), cache.get("tokens")
            return cached_email, cached_token
        except Exception as e:
            raise Exception("Something went wrong trying to cache your email and tokens")
    
    def get_cache() -> tuple:
        try:
            cached_email, cached_token = cache.get("email"), cache.get("tokens")
            return cached_email, cached_token
        except Exception as e:
            return dcc.Link("Oh Dear, Appears you need to Authenticate, Click this to head back to login..", href=login_location)
