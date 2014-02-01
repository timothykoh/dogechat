from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(DogeUser)
admin.site.register(FriendReq)
admin.site.register(Friendship)
admin.site.register(Conversation)