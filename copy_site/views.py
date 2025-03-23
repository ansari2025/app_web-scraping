from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import WebPage
from .utils import store_webpage  # Assuming the function is in utils.py

# Create your views here.
def save_page(request):
    from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLForm
from .utils import store_webpage

def save_page(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            page = store_webpage(url)

            if not page:
                return HttpResponse("Failed to fetch or store the webpage data.", status=500)

           # return HttpResponse(f"Stored Title: {page.title}<br>Stored Div Content: {page.div_content}")

    else:
        form = URLForm()

    return render(request, "save_page.html", {"form": form})


    
   # page = store_webpage(url)
    #if page is None:
      #  return HttpResponse("Failed to fetch or store the webpage.", status=500)

  

    #return HttpResponse(f"Stored content from {page.url}")