

import requests
from bs4 import BeautifulSoup

url = input("Enter the site URL: ").strip()

try:
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)

    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    with open("headings.txt", "w", encoding="utf-8") as f:
        for h in soup.find_all(['h1', 'h2', 'h3']):
            text = h.get_text(strip=True)
            if text:
                f.write(text + "\n")

    print("Headings saved successfully!")

except requests.exceptions.HTTPError as http_err:
    if r.status_code == 404:
        print("Error 404: Page not found.")
    else:
        print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error: {req_err}")
except OSError as file_err:
    print(f"File error: {file_err}")