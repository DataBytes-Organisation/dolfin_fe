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

    def basiq_api_transaction_data(self) -> dict:
        try:
    
            url = self.base_url+"/basiq/transactions"

            payload = {}
            headers = {
                "accepts": "application/json",
                "Authorization": "eyJraWQiOiJcL1pZTmRxczQwRFVHYjE2MFAyNThTVzJnYW0zUXhlSkZMeVlpb3JFck80Zz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMTVlZmQwZS05YjY2LTRjNDctYjM0My1hZTc1YmRmMGI1NTQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfZXZNMHd6ZTRqIiwiY29nbml0bzp1c2VybmFtZSI6ImIxNWVmZDBlLTliNjYtNGM0Ny1iMzQzLWFlNzViZGYwYjU1NCIsIm9yaWdpbl9qdGkiOiJhOGE3ZTUzNC1mMmE1LTQ5YTItYWQ4ZS0zN2MwNGY3ZGVkYTYiLCJhdWQiOiIzOHBwbG1zb2p1ZHNjMDhzZ2wwdWQ0djdqciIsImV2ZW50X2lkIjoiNjIyM2YzODAtZGQ0YS00ZWM5LTgyZmQtM2U4YmMyYmY1MjhiIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODQwMjI2MjUsIm5hbWUiOiJkYW5ubm9yciIsImV4cCI6MTY4NDAyNjIyNSwiaWF0IjoxNjg0MDIyNjI1LCJqdGkiOiI4NGM4ZDk5Yy0xMjlhLTQyNGYtODZiYS1jNmU0MjAxM2RiNmQiLCJlbWFpbCI6ImRhbkBlbWFpbC5jb21tIn0.uM5Jq3-PiT1U_xFph-JFsFDBMvPD7GG9WlfBDP955iTFbzaM9mSnKDVWAqvXkQ6Gr2HkvH9qaVts2R3w1S3dug8sr0iSBmZy7fDBkbE-_OmD4m_LshRF1DqW7jVmmEMF-OyL_s3H-P_VYTawni924pCSSZ7rJ1qIXMXsgxpFKOrC7DwXXAtC_HKGzWGJZu9_JHy7cHseweYOXm9T3pNNMjtdI8BrlYF785jVFVoi6AU0wzx9os7p6xryG9nn4ar6f9ojnpN-gesZt9CxXem-5jO4GvQkGhluDq1ukd0ad6cHBpCe2QwP-yBMNfRQSiW-iCkGoVgOLHDvI1tB3fFjaA"
                }    

            response = requests.request("GET", url, headers=headers, data=payload)
            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            #print(response.json())
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception("Error getting dashboard data failed")
