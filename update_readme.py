import os
import requests
import base64
from github import Github

# GitHub repository information
REPO_NAME = "thivyanth/thivyanth"
FILE_PATH = "README.md"
GITHUB_TOKEN = os.getenv('GH_TOKEN')

# GitHub API URL to fetch the file
REPO = "thivyanth/thivyanth.github.io"
SOURCE_FILE_PATH = "_pages/about.md"
api_url = f"https://api.github.com/repos/{REPO}/contents/{SOURCE_FILE_PATH}"

# Fetch the file content from GitHub
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    file_content = response.json().get('content')
    about_content = base64.b64decode(file_content).decode('utf-8') if file_content else "About section not found."

    # Remove the front matter
    parts = about_content.split('---')
    if len(parts) > 2:
        about_content = '---'.join(parts[2:]).strip()
else:
    about_content = "Failed to fetch About section from GitHub."

# Define the README content
readme_content = f"""
{about_content}
"""

# Initialize GitHub client
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Get the current README file
contents = repo.get_contents(FILE_PATH, ref="main")

# Update the README file
if contents.decoded_content.decode("utf-8") != readme_content:
    repo.update_file(contents.path, "Update README from website", readme_content, contents.sha, branch="main")
else:
    print("No changes detected in README.md")
