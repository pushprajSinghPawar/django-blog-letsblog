from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(''' app home <h1 style="font-size:70px;">
    <a href="http://127.0.0.1:8000/admin"> link to admin </a>
    </br></br></br></hr></hr>
    <a href="http://127.0.0.1:8000/blog"> link to site </a>
    </br></br></br></hr></hr>
    <a href="http://127.0.0.1:8000/admin/blogapp/blogpost/"> link to admin post </a>
    </br></br></br></hr></hr>
    </h1>
    ''')