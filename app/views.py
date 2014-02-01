import json

from django.shortcuts import render
from django.http import (HttpResponseRedirect, HttpResponse)
from django.core.urlresolvers import reverse

from app.models import DogeUser
from django_facebook.api import get_facebook_graph
from open_facebook import OpenFacebook
from django.core import serializers

# Create your views here.
def index(request):
    if request.session.has_key("user_info") == False:
        return HttpResponseRedirect(reverse("login"))
    else:
        print request.session["user_info"]
        # graph = get_facebook_graph(request)
        # facebook_me = graph.get("me")
        # print facebook_me
        # name = facebook_me["name"]
        # email = facebook_me["email"]
        # facebook_id = facebook_me["id"]

        # user_list = User.objects.all()
        # context = {"user_list" : user_list}
        return render(request, "app/index.html")

def login(request):
    return render(request, "app/login.html")

def login_success(request):
    graph = get_facebook_graph(request)
    facebook_me = graph.get("me")
    print facebook_me
    name = facebook_me["name"]
    email = facebook_me["email"]
    facebook_id = facebook_me["id"]

    user_info = {
                    "name" : name,
                    "email" : email,
                    "facebook_id" : facebook_id
    }

    request.session["user_info"] = user_info
    return HttpResponseRedirect(reverse("index"))

def getfriend(request):
    searchTerm = request.GET['term']
    res = DogeUser.objects.filter(name__contains = "")
    data = serializers.serialize('json',res)
    return HttpResponse(data,mimetype='application/json')
