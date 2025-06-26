# 📰 Headline Web Scraper

This is a simple Python script that fetches a webpage and extracts all `<h1>`, `<h2>`, and `<h3>` headings using `requests` and `BeautifulSoup`. The headings are saved into a file named `headings.txt`.

---

## 🚀 Features

- Fetch raw HTML from any URL
- Extract and save all main headings (`h1`, `h2`, `h3`)
- Handles:
  - HTTP errors (like 404)
  - Request issues (e.g. timeout, bad connection)
  - File writing errors

---

## 🛠 Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

  ---

## 🧠 What I Learned

For this project, I first learned how to use the `requests` module to fetch HTML content from websites and then used `BeautifulSoup` to parse and extract specific elements from the page.

This helped me understand:

- How web pages are structured with HTML
- How to extract useful content like headlines using Python
- The difference between HTTP methods and error handling
- Real-world use of Python for automation and data scraping

---


Install dependencies with:

```bash
pip install requests beautifulsoup4
