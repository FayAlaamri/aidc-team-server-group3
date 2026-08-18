# Copy this file, rename it to your GitHub username, and change both fiel>
# The server picks up any file in here that defines PATH and handle().
# Files starting with _ are ignored, so this one never becomes an endpoin>

PATH = "/NewEndpoint"

def handle():
    return {
        "name": "NewEndpoint",
        "team": "Group 3",
        "wants": "I want to change the repo",
    }
