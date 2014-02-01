import json

from django.shortcuts import render
from django.http import (HttpResponseRedirect, HttpResponse)
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from app.models import *
from django_facebook.api import get_facebook_graph
from open_facebook import OpenFacebook
from django.core import serializers

# Create your views here.
def index(request):
    if request.session.has_key("user_info") == False:
        return HttpResponseRedirect(reverse("login"))
    else:
        chat1 = {
                    "nickname" : "Timothy",
                    "facebook_id" : "747108288",
                    "time" : "11:30am",
                    "sent" : 1
                }
        chat2 = {
                    "nickname" : "Foo Lai",
                    "facebook_id" : "choo.f.lai",
                    "time" : "12:22pm",
                    "sent" : 1
                }
        chat3 = {
                    "nickname" : "Vincent",
                    "facebook_id" : "vincom2",
                    "time" : "4:31pm",
                    "sent" : 0
                }
        chat_list = [chat1, chat2, chat3]
        context = {"chat_list" : chat_list}
        return render(request, "app/index.html", context)

def login(request):
    return render(request, "app/login.html")

def login_success(request):
    graph = get_facebook_graph(request)
    facebook_me = graph.get("me")
    print facebook_me
    name = facebook_me["name"]
    email = facebook_me["email"]
    facebook_id = facebook_me["id"]

    try:
        curUser = DogeUser.objects.get(facebook_id=facebook_id)
    except ObjectDoesNotExist:
        curUser = DogeUser.objects.create_user(email,name,facebook_id)
    
    primary_id = curUser.id
        
    user_info = {
                    "name" : name,
                    "email" : email,
                    "facebook_id" : facebook_id,
                    "primaryID" : primary_id
    }

    request.session["user_info"] = user_info

    return HttpResponseRedirect(reverse("index"))

def getfriend(request):
    searchTerm = request.GET['term']
    res = DogeUser.objects.filter(name__contains = "")
    data = serializers.serialize('json',res)
    return HttpResponse(data,mimetype='application/json')

def getContacts(request):
    fb_id = request.GET['user_id']
    curUser = DogeUser.objects.get(facebook_id=fb_id)
    friends = FriendMan.friends_of(curUser)
    info = []
    for friend in friends:
        info.append(friend.get_Details())
    infoDict = {"contactInfo":info}
    contactData = serializers.serialize('json',infoDict)
    return render(request,"app/people.html",contactData,content_type = 'application/json')

