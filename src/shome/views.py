import pathlib
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request):
    context = {
        "title" : "SaaS | Home",
        "name" : "IDIOT"
    }
    # html_file_path = this_dir / "home.html"
    # html_ = html_file_path.read_text()
    return render(request, "home.html", context)