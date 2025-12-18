from bs4 import BeautifulSoup
import requests

# URL of the page
url = "https://en.wikipedia.org/wiki/Hamburger"

# Get page HTML
headers = {"User-Agent": "Mozilla/5.0"}  # Wikipedia likes a user-agent
response = requests.get(url, headers=headers)
html = response.text

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Extract page title safely
h1 = soup.find("h1")
title = h1.get_text(strip=True) if h1 else "No title found"

# Extract first paragraph safely
p = soup.find("p")
first_para = p.get_text(strip=True) if p else "No paragraph found"

print("Title:", title)
print("Paragraph:", first_para)
