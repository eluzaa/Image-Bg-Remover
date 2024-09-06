import requests

url = "https://background-remover.p.rapidapi.com/remove-background"

image_file_path = "test.png"
# Opening the uploaded file and here we used 'rb' mode as image is read as binary data
with open(image_file_path, 'rb') as image_file:
    files = {
        'image': image_file
    }

    headers = {
        "x-rapidapi-key": Your API Key,
        "x-rapidapi-host": "background-remover.p.rapidapi.com"
    }

    response = requests.post(url, files=files, headers=headers)
    print(f"Status Code: {response.status_code}")

    # Try to decode the response as JSON
    try:
        response_data = response.text
        with open("link.json", 'a') as images:
            images.write(response_data)
    except requests.exceptions.JSONDecodeError:
        # If it's not JSON, print the raw response
        print("Response content is not valid JSON")
        # print(response.text)
