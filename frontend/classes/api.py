import os
from environment.settings import base_api_url
import requests
import json

class API:
    """this class acts as the interface between front end and backend, 
    if you have deployed the backend you will need to change the BASE_API_URL
    is the environment > .env and/or environment .env.development file(s)"""
    def __init__(self) -> None:
        self.base_url = base_api_url
    
    def sign_up(self, fname: str, lname: str, nname: str, email: str, password: str) -> dict:
        try:
    
            url = self.base_url+"/auth/account/user"

            payload = json.dumps({
            "first": fname,
            "last": lname,
            "nickname": nname,
            "email": email,
            "password": password,
            "role": 0
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception(f"Sign up for user : {email} failed")
    
    def sign_in(self, email: str, password: str) -> dict:
        try:
            url = self.base_url+"/auth/account/user?email="+email+"&password="+password

            response = requests.request("GET", url, headers={}, data={})
            if response.status_code > 299:
                raise Exception(f"The Sign in Request has failed, likely due to issue with email or password")
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception(f"Sign in for user : {email} failed, likely due to backend being down")
    
    def refresh_token_auth(self, email: str, tokens: dict) -> dict:
        try:
            refresh_token = tokens.get('RefreshToken')
            id_token = tokens.get('IdToken')
            
            url = f"{self.base_url}/auth/token/refresh?refresh_token={refresh_token}"
            headers = {
            'Authorization': f'{id_token}'
            }

            response = requests.request("GET", url, headers=headers, data={})
            if response.status_code > 299:
                raise Exception(f"There was an issue getting a refresh token")
            return json.loads(response.text)
        except Exception as e:
            raise Exception(f"There was an issue getting a refresh token")

    
        