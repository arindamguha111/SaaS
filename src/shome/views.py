import pathlib
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


this_dir = pathlib.Path(__file__).resolve().parent

def base_view(request):
    context = {
        "title" : "SaaS",
        "message" : "Welcome To Django"
    }
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return render(request, "base.html", context)

def home(request):
    context = {
        "title" : "Homepage",
        "message" : "Welcome to the Home Page"
    }
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return render(request, "home.html", context)