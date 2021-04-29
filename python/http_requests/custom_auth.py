import requests
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme"""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach API token to a custom auth header"""
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r


requests.get('https://httpbin.org/get', auth=TokenAuth('1233e3e3e'))
