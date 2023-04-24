import os
from environment.settings import base_api_url

class API:
    """this class acts as the interface between front end and backend, 
    if you have deployed the backend you will need to change the BASE_API_URL
    is the environment > .env and/or environment .env.development file(s)"""
    def __init__(self) -> None:
        self.base_url = base_api_url
        print(self.base_url)
    
    def sign_up(self, email: str, password: str) -> dict:
        """this request that performs sign up goes here"""
        raise NotImplementedError("this has not been implemented yet")
    
    def sign_in(self, email: str, password: str, first: str, last: str) -> dict:
        """this request that performs sign in goes here"""
        raise NotImplementedError("this has not been implemented yet")
        
# class BE_API:
#     def __init__(self) -> None:
#         self.backend_api_url = backend_api_url
#         print(self.backend_api_url)