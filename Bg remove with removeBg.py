import requests


url = 'https://api.remove.bg/v1.0/removebg'
api_key = 'APK5XHQjJjrqFf22UH1JYAZF'

response = requests.post(
    url,
    files={'image_file': open('test.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': api_key},
)


if response.status_code == requests.codes.ok:
    # Basically here i am creating a new file (no-bg) and writing binary content in it...
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)