
# Python Image Background Remover

## Description

This project offers two versions of a Python-based application for removing backgrounds from images using API calls. One version utilizes the **remove.bg API**, while the other leverages the **RapidAPI** service for background removal. The application takes an image as input and returns a processed image with the background removed.

### Note

You may not get the removed bg imgae if you API quota is reached. So please check the pricing and API calss details also.

## Features

- **Version 1: remove.bg API**: Processes images using the popular remove.bg service for background removal.
- **Version 2: RapidAPI**: Uses the RapidAPI platform to call different background removal services.
- **Python-Based**: Both versions use Python for API calling and image processing.
- **Efficient and Simple**: Easily remove image backgrounds by calling the appropriate API.

## Technologies Used

- **Python**: The core language used for building the application.
- **APIs**:
  - **remove.bg API**: Provides high-quality background removal for images.
  - **RapidAPI**: Allows flexibility in choosing different background removal services.
- **Libraries**:
  - `requests`: For making HTTP requests to the APIs.
  - `io`: For handling image data in memory.
  - `Pillow`: For image processing (optional).

## Setup and Usage

### Version 1: remove.bg API

1. Install required dependencies:

   \`\`\`bash
   pip install requests Pillow
   \`\`\`

2. Set up your remove.bg API key in the code.

3. Run the script:

   \`\`\`bash
   python remove_bg_version.py
   \`\`\`

### Version 2: RapidAPI

1. Install required dependencies:

   \`\`\`bash
   pip install requests Pillow
   \`\`\`

2. Set up your RapidAPI key and chosen service in the code.

3. Run the script:

   \`\`\`bash
   python rapidapi_version.py
   \`\`\`

## Prerequisites

- A valid API key from [remove.bg](https://www.remove.bg/) or [RapidAPI](https://rapidapi.com/).
- Python 3.x installed on your machine.

## Example Usage

In both versions, you provide an image, and the application will remove the background and save the processed image. 

1. **remove.bg API Example**:

   ```python
   response = requests.post(
       'https://api.remove.bg/v1.0/removebg',
       files={'image_file': open('input.png', 'rb')},
       data={'size': 'auto'},
       headers={'X-Api-Key': 'your_api_key'}
   )
   ```

2. **RapidAPI Example**:

   ```python
   response = requests.post(
       'https://rapidapi-endpoint-url.com/remove',
       files={'image_file': open('input.png', 'rb')},
       headers={
           'X-RapidAPI-Key': 'your_rapidapi_key',
           'X-RapidAPI-Host': 'api-host'
       }
   )
   ```

## Acknowledgments

- [remove.bg API](https://www.remove.bg/) for their excellent background removal service.
- [RapidAPI](https://rapidapi.com/) for providing access to multiple API services for background removal.

## License

This project is not licensed under the MIT License :)
