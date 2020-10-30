import requests

response = requests.get('https://api.github.com')

if response:
    print('Success')
else:
    print('Error occured!')