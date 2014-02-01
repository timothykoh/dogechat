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
        user = curUser["primary_id"]
        curChat = Conversation.objects.getConvo(user)
        num = 0
        chat_list = []
        for i in curChat:
            chat_list.append(i.getDetails)
            num += 1    
        
        friends = Friendship.objects.friends_of(user)
        info = [("hello", 1),("byebye",2)]
        for friend in friends:
            info.append(friend.get_Details())
#         chat_list = [
#         {
#             "msg_id" : "1",
#             "facebook_id" :"34324221",
#             "sender" : "43",
#             "timeSent" : "12",
#             "dogetext" : "much doge,so amaze,much help,wow,much cool,very wow"
# 
#         }]
        context = {"chat_list" : chat_list, "contact_info" : info}
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
    sender = request.session['sender_pri_id']
    curUser = request.session['user_info']
    rec = curUser['primary_id']
    getChat = Conversation.objects.get(msg_id = curChat)
    checkSend = (getChat.sender_pri_id == sender)
    checkRec = getChat.rec_pri_id == rec
    if (checkRec and checkRec):
        getChat.boolRead = True
        getChat.save()
        

def startChat(request):
    curUser = request.session["user_info"]
    sender_pri_id = curUser['primary_id']
    sender_fb_id = curUser['facebook_id']
    
    rec_pri_id = request.session["rec_pri_id"]
    rec_fb_id = DogeUser.objects.get(id = rec_pri_id).get_fb_id()
    
    msg = request.session['dogetext']
    dogemsg = to_doge(msg)
    
    newC = Conversation.objects.createConvo(
        sender_pri_id,sender_fb_id,
        rec_pri_id, rec_fb_id,
        dogemsg)
    return render(request,"app/index.html")

def askFriend(request):
    curUser = request.session["user_info"]
    from_user = DogeUser.objects.get(id = curUser['primary_id'])
    friend = request.session['friend_pri_id']
    to_user = DogeUser.objects.get(id = friend)
    newReq = FriendReq.objects.create(from_user = from_user,to_user = to_user)
    newReq.accept() # accept first for now
    return render(request,"app/index.html")
