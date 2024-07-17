import os
from bs4 import BeautifulSoup
import requests

# URL of your website
url = "https://thivyanth.github.io"

# Fetch the About Me content from your website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the necessary information (assuming it's in a div with class 'about')
about_section = soup.find('div', class_='about')
about_content = about_section.get_text(separator="\n") if about_section else "About section not found."

# Define the README content
readme_content = f"""
{about_content}
"""

# Write the content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
