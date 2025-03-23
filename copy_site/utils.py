import requests
from bs4 import BeautifulSoup
from .models import WebPage


import requests
from bs4 import BeautifulSoup
from .models import WebPage

def store_webpage(url):
  #  """Fetch and store webpage content in the database"""
    try:
        print(f"Fetching URL: {url}")  # Debugging print

        headers = {"User-Agent": "Mozilla/5.0"}  # Pretend to be a browser
        response = requests.get(url, headers=headers, timeout=10)  # Add timeout

        response.raise_for_status()  # Raises an error for HTTP failures (4xx, 5xx)
        
        soup = BeautifulSoup(response.text, "html.parser")
        #content = soup.prettify()
        #content = soup.title.string.strip() if soup.title else "No Title Found"

# Extract first <div> with a specific class or just the first <div>
        div_content = ""
        div = soup.find("li")  # You can customize this: soup.find("div", {"class": "target-class"})
        if div:
            div_content = div.get_text(strip=True)  # Get text without extra spaces
        content = div_content
        # Check if the page is already in the database
        page, created = WebPage.objects.get_or_create(url=url, defaults={'content': content})

        if not created:  # If it already exists, update content
            page.content = content
            page.save()

        print(f"Successfully stored content from: {url}")  # Debugging print
        return page  # Return the saved page object

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")  # Print the actual error in terminal
        return None  # Return None if there's a request failure
