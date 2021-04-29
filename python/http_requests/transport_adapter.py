import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

git_adapter = HTTPAdapter(max_retries=3)
session = requests.Session()

# Mount the adapter to the session
session.mount('https://api.github.com', git_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
