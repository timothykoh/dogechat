import json

from django.shortcuts import render
from django.http import (HttpResponseRedirect, HttpResponse)
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from app.models import *
from django_facebook.api import get_facebook_graph
from open_facebook import OpenFacebook
from django.core import serializers

from dogeify.dogeify import to_doge

# Create your views here.
def index(request):
    if request.session.has_key("user_info") == False:
        return HttpResponseRedirect(reverse("login"))
    else:
        curUser = request.session["user_info"]
        name = curUser["name"]
        email = curUser["email"]
        facebook_id = curUser["facebook_id"]
        user = DogeUser.objects.get(id = curUser["primary_id"])
        curChat = Conversation.objects.getConvo(user)
        num = 0
        chat_list = []
        for i in curChat:
            chat_list.append(i.getDetails)
            num += 1    
        
        friends = Friendship.objects.friends_of(user)
        info = []
        for friend in friends:
            info.append(friend.get_Details())

        context = {"chat_list" : chat_list, "contact_info" : info}
        return render(request, "app/index.html", context)

def login(request):
    print to_doge("hey this is going to be doge")
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
                    "primary_id" : primary_id
    }

    request.session["user_info"] = user_info

    return HttpResponseRedirect(reverse("index"))

def getfriend(request):
    searchTerm = request.GET['term']
    num = request.GET['num']
    start = request.GET['start']
    
    res = DogeUser.objects.filter(name__contains = searchTerm)
    
    data = serializers.serialize('json',res)
    return HttpResponse(data,mimetype='application/json')

def read(request):
    curChat = request.session['msg_id']
    sender = request.session['sender_id']
    curUser = request.session['user_info']
    rec = DogeUser.objects.get(id = curUser['primary_id'])
    

def startChat(request):
    curUser = request.session["user_info"]
    user = DogeUser.objects.get(id = curUser["primary_id"])
    #someone needs to do what kind of event submit is used to let me know who he clicked on
    
    newC = Conversation.objects.createConvo(user,rec,msg)
    return render(request,"app/index.html")
