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

    def dashboard(self) -> dict:
        try:
    
            url = self.base_url+"/basiq/transactions"

            payload = {}
            headers = {
                "accepts": "application/json",
                "Authorization": "eyJraWQiOiJOT0RocDQ3NVNVOWxZN3IzdkcxdU5PbW81bGVuSmFsZ3FFb3lFZ1g2TmJZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJlN2IzMDkwOS1mY2Q5LTRkYjctYWY0ZS0zMTIxZjBjMjc3NWYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfMFRDak1zODluIiwiY29nbml0bzp1c2VybmFtZSI6ImU3YjMwOTA5LWZjZDktNGRiNy1hZjRlLTMxMjFmMGMyNzc1ZiIsIm9yaWdpbl9qdGkiOiI0Zjg2OGZlMy01YWZkLTRiZGYtOWRmNi1lYzEwYmI4YzE4MjciLCJhdWQiOiJrajgybXBmaG0wZWd1MTNmM2w5bTEyNWs1IiwiZXZlbnRfaWQiOiI1NDdmMjE0Zi0xNGFjLTQwZDYtOGQ2Mi04MGRkMTBkM2NlMTgiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4Mjk1MDkyNiwibmFtZSI6ImZha2VmaXJzdGZha2VsYXN0IiwiZXhwIjoxNjgyOTU0NTI2LCJpYXQiOjE2ODI5NTA5MjYsImp0aSI6IjBkMDllZTM0LTY2NTAtNDIxYi05YzdkLThhZTIwMjJiNTYzOCIsImVtYWlsIjoieW91ci1lbWFpbEB0ZXN0LnRlc3R0In0.ItwuuxSw2YCtR-bff7EXgFhWXSJ4jnhl_sJAu_rFZJzrD5sdIaJ8sZkHSrSe87Go5RVQQNSW7bgI6lEd7Y_1605lyUPN79FF7-RwGEJKe1oFuRGMbIrrEU7yVs0NGh2CxKevKeNqUkySJsepIqU4kjLPYbTkB7TzkLa-27oF0l3zt7KPsm6S7Aky8pO6v_K6AT9Zeovk4Q_-yd1TzLdhl4k6y_tm6_ogBT-5vOu_UsCY8jECIKtagEY9XsCsZeG9yuENwr4rsy8Zq7FK0ZPz8KOBLgysF8dY_S6SR_IGu5OxzKlqyhkJO2UIl56F6NfCPcy2tGFFAvkLgE9wSOd2vw"
                }    

            response = requests.request("GET", url, headers=headers, data=payload)
            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            #print(response.json())
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception("Error getting dashboard data failed")

    def get_accounts(self) -> dict:
        try:
    
            url = self.base_url+"/basiq/accounts"

            payload = {}
            headers = {
                "accepts": "application/json",
                "Authorization": "eyJraWQiOiJOT0RocDQ3NVNVOWxZN3IzdkcxdU5PbW81bGVuSmFsZ3FFb3lFZ1g2TmJZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJlN2IzMDkwOS1mY2Q5LTRkYjctYWY0ZS0zMTIxZjBjMjc3NWYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfMFRDak1zODluIiwiY29nbml0bzp1c2VybmFtZSI6ImU3YjMwOTA5LWZjZDktNGRiNy1hZjRlLTMxMjFmMGMyNzc1ZiIsIm9yaWdpbl9qdGkiOiJjYTg2Y2U0Yy1kNDc2LTQ0MjktYmYzNi0xMDMzYzkyNmM5YmMiLCJhdWQiOiJrajgybXBmaG0wZWd1MTNmM2w5bTEyNWs1IiwiZXZlbnRfaWQiOiIxNzdhYjhiOC05MDk4LTQ0M2YtOGNkZi0xYzUwZGVjMWIxZDgiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY4Mjk0NzI1NywibmFtZSI6ImZha2VmaXJzdGZha2VsYXN0IiwiZXhwIjoxNjgyOTUwODU3LCJpYXQiOjE2ODI5NDcyNTcsImp0aSI6IjIwNWIyOWIwLWUwYjEtNGNlNC1hMTBjLTRlYzBkODhiNGQyNCIsImVtYWlsIjoieW91ci1lbWFpbEB0ZXN0LnRlc3R0In0.BTSimgeR5uBf9vyJXArW9aqzLNMWGy8z71vSx5W2fMalq-iUwRKYERYIZjjc7TY7UMeMy0vVL9eBNtkjddNCmEYIVgH-xZqLy8sSnUwLQc4QnxwIRFxQJy379po3o3xL7_EKKspENTHAcJXSKDqjuFOy8RRngyfGJ7BqO3JY2fimvE3W4saBPi12-yKFUb6Cvb1TX1PL7EoVjO33VB2dK1zwoV2OH5676arAR16xZzffivdwfGemet_hTljQyraY97qmOsjKOu4ddBjC_JUA8n4GDcYylIgKCHHNMlihn1t0B29bbQgk2i_0voqaJi26ZmBLAlWyi5GYlbmjqSzwRA"
                }    

            response = requests.request("GET", url, headers=headers, data=payload)
            if response.status_code > 299:
                raise Exception("HTTP {response.statuscode} Bad Status Code")
            #print(response.json())
            return json.loads(response.text)
        
        except Exception as e:
            raise Exception("Error getting dashboard data failed")
        
class BE_API:
    def __init__(self) -> None:
        self.backend_api_url = backend_api_url
        print(self.backend_api_url)