import requests

# search github repositories for requests
response = requests.get('https://api.github.com/search/repositories',
                        params={'q':'requests+language:python'},)

# inspect some attributes
json_resp = response.json()
repo = json_resp['items'][0]
print(f'Repo:{repo["name"]}')
print(f'Repo Description:{repo["description"]}')
