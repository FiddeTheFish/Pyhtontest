import requests

x= requests.get('https://www.google.com')

if x.status_code == 200:
    print('Yay')
else
print('Shit')

