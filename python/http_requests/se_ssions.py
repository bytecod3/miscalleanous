import requests
from getpass import getpass

with requests.Session() as session:
    session.auth = ('username', getpass())
    response = session.get('https://api.github.com') # to persist user credentials across the connection

# inspect the response
print(response.headers)
print(response.json())

