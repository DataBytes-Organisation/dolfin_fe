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

    # def dashboard(self) -> dict:
    #     try:
    
    #         url = self.base_url+"/basiq/transactions"

    #         payload = {}
    #         headers = {
    #             "Authorization": "eyJraWQiOiJRRU5nQ0V4OVwvcGp4NnhsQXZrYnVcL0RrN1VKc0lDQm5Zend5VHd2THVzdW89IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwOTY0NTU5Ny1jNWQ1LTQwZjUtOTljZi1mYjg1NGYyMTU5ZTMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTIuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTJfQXRoaWVpeWphIiwiY29nbml0bzp1c2VybmFtZSI6IjA5NjQ1NTk3LWM1ZDUtNDBmNS05OWNmLWZiODU0ZjIxNTllMyIsIm9yaWdpbl9qdGkiOiIyNjNjZWNkNy01ZWI0LTQyYzctOTQxZS1jYmYxZDQyMjU3ZTYiLCJhdWQiOiIxOTBlMjFtcTg0amtyMjM2bzQ3ZTBpY3JubSIsImV2ZW50X2lkIjoiMmYxNzRmYWYtMjUzMy00YmFhLTk5ZjItNmY0Nzk2YTNmOGRkIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2ODI4NDMxOTMsIm5hbWUiOiJmYWtlZGFuZmFrZW5vciIsImV4cCI6MTY4Mjg0Njc5MywiaWF0IjoxNjgyODQzMTkzLCJqdGkiOiJiY2ZmM2U5Ny0xY2MxLTRmYjYtYTFlMi0xMTgzNjEzMTYyZDciLCJlbWFpbCI6ImZha2VkYW5ub3JAZ21tYWFpbC5jb20ifQ.sa1tGQAbDYBeq35hdmR2h8MR9tCoG293AuJLVEt7P0gzSDZwrSYGeAELA1BbzEG3p0_e3zjjMIe7WxRKaoEtzJ78vpfCcekjDDhSZ9-bZl7msUhDFIQyomAxsddmnRUkqfUlYEbZDoEderKcQzQvxMrsRuy8Z7nDKNBRoN9Bv8KBUGCgU8dXIX7FfELIM6LVPzPgzEtE_M6_e4gUKeUDi-4zPwOPb_1I2sEKnxDZCCFn7m2V7q35a0YlRXKI93d0-0H7NhOX0BnOW6fOuy9n8CiXCqhu_ynOLFV27OpPWZpT9L7-ydLHAsevFqNFwWFK3lLhQhZHc3sDJ1LEX4lmng"
    #         }    

    #         response = requests.request("GET", url, headers=headers, data=payload)
    #         if response.status_code > 299:
    #             raise Exception("HTTP {response.statuscode} Bad Status Code")
    #         #print(response.json())
    #         return json.loads(response.text)
        
    #     except Exception as e:
    #         raise Exception("Error getting dashboard data failed")
        
# class BE_API:
#     def __init__(self) -> None:
#         self.backend_api_url = backend_api_url
#         print(self.backend_api_url)