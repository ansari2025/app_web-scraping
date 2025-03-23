from django.db import models
from .models import WebPage

def store_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.prettify()
        
        # Save to the database
        page, created = WebPage.objects.get_or_create(url=url, defaults={'content': content})
        if not created:
            page.content = content
            page.save()
        return page
