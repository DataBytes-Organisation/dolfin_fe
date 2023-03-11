import os
from environment.settings import base_api_url

class API:
    def __init__(self) -> None:
        self.base_url = base_api_url
        print(self.base_url)