from django.shortcuts import render

from app.models import User
from django_facebook.api import get_facebook_graph
from open_facebook import OpenFacebook


# Create your views here.
def index(request):
    graph = get_facebook_graph(request)
    print graph.get("me")
    user_list = User.objects.all()
    context = {"user_list" : user_list}
    return render(request, "app/index.html", context)

def login(request):
    return render(request, "app/login.html")