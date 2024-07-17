import os
import requests
import base64

# GitHub repository information
REPO = "thivyanth/thivyanth.github.io"
FILE_PATH = "_pages/about.md"
GITHUB_TOKEN = os.getenv('GH_TOKEN')

# GitHub API URL to fetch the file
api_url = f"https://api.github.com/repos/{REPO}/contents/{FILE_PATH}"

# Fetch the file content from GitHub
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    file_content = response.json().get('content')
    about_content = base64.b64decode(file_content).decode('utf-8') if file_content else "About section not found."
else:
    about_content = "Failed to fetch About section from GitHub."

# Define the README content
readme_content = f"""
{about_content}
"""

# Write the content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
