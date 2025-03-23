from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label="Enter Website URL", widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "https://example.com"}))
