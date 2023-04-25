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
        print(self.base_url)
    
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
            #print(response.json())
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception(f"Sign up for user : {email} failed")
    
    def sign_in(self, email: str, password: str) -> dict:
        try:
    
            url = self.base_url+"/auth/account/user?email="+email+"&password="+password

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception(f"Sign in for user : {email} failed")
        