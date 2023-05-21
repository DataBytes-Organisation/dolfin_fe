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
                "Authorization": "eyJraWQiOiJlcXhraW1yN21mRkwySmpjMmx1ZCtuT0JlNk5DVU00aHNMaEtta1p6MjVRPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJlN2NlM2ZhYy0zOGNjLTRiNjAtOTc4MC1jMDBiMTZjYmI3OTYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfNzNlY0FOdWRNIiwiY29nbml0bzp1c2VybmFtZSI6ImU3Y2UzZmFjLTM4Y2MtNGI2MC05NzgwLWMwMGIxNmNiYjc5NiIsIm9yaWdpbl9qdGkiOiI2ODFmNjBmNy01YjIzLTQzYzItYjA0OC03OWFkNmQyYTgyNzUiLCJhdWQiOiI1N2kzOW9xcG1wdGIxZmxxZmoxdXUzaWJwYSIsImV2ZW50X2lkIjoiYTJlNTc0OTAtMDQzZS00ZGI4LTk0MzktNGI0ZGNlZGJlMWI1IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODQzNTkzNTYsIm5hbWUiOiJkYW5ubm5vcnIiLCJleHAiOjE2ODQzNjI5NTYsImlhdCI6MTY4NDM1OTM1NiwianRpIjoiNGEwM2JlNmItNTM5NC00MWRlLWFiMGEtMTQwOWNhMzk0MzZlIiwiZW1haWwiOiJkYW5AZW1haWwuY29tbSJ9.ZVlGgqM_Bxz1IdF65eN097rh0KBUeVxkw2zm806uwqpAeiGoxGXjJYVLx3kIwcSk50dhqNCu5_MZqt9lIfHNobFGs7Xjz-g2GVEPDttMELqllmCGier9m8QjhAmE3VJ3TwXbR1-oN1IxPkJe4slxKiFKN4OMqdZpAYETsfX0IJc2WQFrC4A00LYmgTLD4Uk0lxToGStsqK3UOp4ZZhmzRUfbKYgOcfNIGvpuUqWmHFjqtxgSG2g5s7Wa1QCloLmIadL3GEOqw8ulTS_BoPNYusy2VW63VSJX2VjO3DPYY41ViBBnaE7Ih7TuuTNiE4mVetBN8XZJ5bLdc4UuMvtFhw"
                }    

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            #print(response.json())
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception("Error getting dashboard data failed")

    def get_accounts_for_user(self) -> dict:
        basiq_id="11103cba-4a08-4397-84a5-22ac125ed2f6"
        try:
            url = self.base_url + "/basiq/balance"

            payload = {}
            headers = {
                "accepts": "application/json",
                "Authorization": "eyJraWQiOiJlcXhraW1yN21mRkwySmpjMmx1ZCtuT0JlNk5DVU00aHNMaEtta1p6MjVRPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJlN2NlM2ZhYy0zOGNjLTRiNjAtOTc4MC1jMDBiMTZjYmI3OTYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfNzNlY0FOdWRNIiwiY29nbml0bzp1c2VybmFtZSI6ImU3Y2UzZmFjLTM4Y2MtNGI2MC05NzgwLWMwMGIxNmNiYjc5NiIsIm9yaWdpbl9qdGkiOiI2ODFmNjBmNy01YjIzLTQzYzItYjA0OC03OWFkNmQyYTgyNzUiLCJhdWQiOiI1N2kzOW9xcG1wdGIxZmxxZmoxdXUzaWJwYSIsImV2ZW50X2lkIjoiYTJlNTc0OTAtMDQzZS00ZGI4LTk0MzktNGI0ZGNlZGJlMWI1IiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODQzNTkzNTYsIm5hbWUiOiJkYW5ubm5vcnIiLCJleHAiOjE2ODQzNjI5NTYsImlhdCI6MTY4NDM1OTM1NiwianRpIjoiNGEwM2JlNmItNTM5NC00MWRlLWFiMGEtMTQwOWNhMzk0MzZlIiwiZW1haWwiOiJkYW5AZW1haWwuY29tbSJ9.ZVlGgqM_Bxz1IdF65eN097rh0KBUeVxkw2zm806uwqpAeiGoxGXjJYVLx3kIwcSk50dhqNCu5_MZqt9lIfHNobFGs7Xjz-g2GVEPDttMELqllmCGier9m8QjhAmE3VJ3TwXbR1-oN1IxPkJe4slxKiFKN4OMqdZpAYETsfX0IJc2WQFrC4A00LYmgTLD4Uk0lxToGStsqK3UOp4ZZhmzRUfbKYgOcfNIGvpuUqWmHFjqtxgSG2g5s7Wa1QCloLmIadL3GEOqw8ulTS_BoPNYusy2VW63VSJX2VjO3DPYY41ViBBnaE7Ih7TuuTNiE4mVetBN8XZJ5bLdc4UuMvtFhw"
                }    

            response = requests.request("GET", url, headers=headers)
            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            #print(response.json())
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception("Error getting account details failed")
