# Available versions
# forge, mohist, fabric, vanilla, paper

# You can install mohist after installing forge from the manage menu
# You can install paper after installing vanilla from the manage menu
# You can install purpur after installing fabric from the manage menu

# Ngrok regions
# Code          Location
#-----------    ---------------------------
# ap            Asia / Pacific (Singapore)
# au            Australia (Sydney)
# eu            Europe (Frankfurt)
# in            India (Mumbai)
# jp            Japan (Tokyo)
# sa            South America (São Paulo)
# us            United States (Ohio)
# us-cal-1      United States (California)

# Do not touch anything below this line, you may damage it
import requests, os, base64

# Check if .gitignore does not exist
if not os.path.exists("./.gitignore"):
    # Base64 encoded string for .gitignore content
    big = "L1B5dGhvbioNCi93b3JrX2FyZWEqDQovc2Vydmlkb3JfbWluZWNyYWZ0DQovbWluZWNyYWZ0X3NlcnZlcg0KL3NlcnZpZG9yX21pbmVjcmFmdF9vbGQNCi90YWlsc2NhbGUtY3MNCi90aGFub3MNCi9zZXJ2ZXJzDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioubXNwDQoqLm91dHB1dA=="
    # Decode the base64 string
    dec = base64.standard_b64decode(big).decode()
    # Write the decoded content to .gitignore
    with open(".gitignore", 'w') as giti:
        giti.write(dec)

# Function to download the latest release
def download_latest_release(download_path='.'):
    # URL of the mirror for the latest release
    mirror = "https://elyxdev.github.io/latest"
    # Send a GET request to the mirror
    pet = requests.get(mirror)
    if pet.status_code == 200:
        # If the request is successful, parse the JSON response
        data = pet.json()
        # Get the URL of the latest release
        url = data.get('url')
        # Extract the version from the URL
        version = url.split("/")[-1]
        # Create the full path for the downloaded file
        pathto = os.path.join(download_path, version)
        # Download the content of the release and save it to the file
        with open(pathto, 'wb') as archivo:
            archivo.write(requests.get(url).content)
        # Return the version (filename)
        return version

# Download the latest release and store the filename
flnm = download_latest_release()
# If the file is a compiled Python file (.pyc)
if flnm.split(".")[-1] == "pyc":
    # Execute the .pyc file using Python 3
    os.system(f"python3 {flnm}")
else:
    # Otherwise, make the file executable and run it
    os.system(f"chmod +x {flnm} && ./{flnm}")
