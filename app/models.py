import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

# Create your models here.
class DogeManager(BaseUserManager):

    def _create_user(self,email,is_manager,name,
        facebook_id):
        now = timezone.now()
        user = self.model(nickname = name, email = email, 
                    is_manager = is_manager,name = name,is_active = True,
                    date_joined = now, facebook_id = facebook_id)
        user.save()
        Friendship.objects.create(user = user)
        return user

    def create_user(self,email,name,facebook_id):
        return self._create_user(email,False,name,facebook_id)

    def create_superuser(self,email,name,facebook_id):
        return self._create_user(email, True,name,facebook_id)  

class DogeUser(AbstractBaseUser):
    nickname = models.CharField(max_length=100,blank = False,unique = False)
    name = models.CharField(max_length=100,blank = False)
    email = models.EmailField(max_length = 254, unique = True)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(default = timezone.now)
    is_manager = models.BooleanField(default = False)
    facebook_id = models.BigIntegerField(blank = False, unique = True)
    
    objects = DogeManager()
    
    def __unicode__(self):
        return "%s" % (self.name)
    
    def get_nick(self):
        return "%s" % (self.nickname)
    
    def get_Details(self):
        return ("%s" % (self.name), "%s" % (self.facebook_id))
    
    class Meta:
        ordering = ('name',)

class FriendReq(models.Model):
    
    from_user = models.ForeignKey(DogeUser,related_name="friendreq_from")
    to_user = models.ForeignKey(DogeUser,related_name="friendreq_to")
    created = models.DateTimeField(default = timezone.now())
    accepted = models.BooleanField(default = False)
    
    def __unicode__(self):
        return u'%(from_user)s wants to be friends with %(to_user)s' % {
                'from_user': unicode(self.from_user.get_nick),
                'to_user': unicode(self.to_user.get_nick),
                }
    def accept(self):
        Friendship.objects.befriend(self.from_user,self.to_user)
        self.accepted = True
        self.save()
    
    def decline(self):
        self.delete()
        
    def cancel(self):
        self.delete()   

class FriendMan(models.Manager):
    def friends_of(self,user):
        return DogeUser.objects.filter(friendship__friends__user = user)
    
    def are_friends(self,user1,user2):
        friendship = Friendship.objects.get(user=user1)
        return bool(friendship.friends.filter(user=user2).exists())
    
    def befriend(self,user1,user2):
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.add(Friendship.objects.get(user=user2))
        FriendReq.objects.filter(from_user=user1,to_user=user2).delete()
    
    def unfriend(self,user1,user2):
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.remove(Friendship.objects.get(user=user2))
        FriendReq.objects.filter(from_user=user1,to_user=user2).delete()
        FriendReq.objects.filter(from_user=user2,to_user=user1).delete()         
      
class Friendship(models.Model):
    user = models.OneToOneField(DogeUser,related_name="friendship")
    friends = models.ManyToManyField('self',symmetrical = True)
    
    class Meta:
        verbose_name = u'friendship'
        verbose_name_plural = u'friendships'
        
    objects = FriendMan()
        
    def __unicode__(self):
        return u'%(user)s\'s friends' % {'user': unicode(self.user.get_nick}
    
    def friend_count(self):
        return self.friends.count()

class ConvoManager(models.Manager):
    def getConvo(self,user):
        return Conversation.objects.filter(rec = user)
    
    def createConvo(self,send,rec,msg):
        check = Friendship.objects.are_friends(send,rec)
        if check:
            return 
            Conversation.objects.create(sender = send, rec = rec, convo1 = msg)

class Conversation(models.Model):
    msg_id = models.AutoField(primary_key = True)
    sender = models.ForeignKey(DogeUser,related_name='msg_sender')
    rec = models.ForeignKey(DogeUser,related_name='msg_rec')
    boolRead = models.BooleanField(default = False)
    
    timeSent = models.DateTimeField(blank = False,auto_now_add=True)
    
    convo1 = models.TextField() 
    
    def getDetails(self):
        return { 
            'msg_id' : "%s" % (msg_id),
            'sender' : "%s" % sender.get_nick,
            'rec' : "%s" % rec.get_nick,
            'boolRead' : "%s" % boolRead,
            'timeSent' : "%s" % timeSent,
            'convo1' : "%s" % convo1
                }
                
    
    objects = ConvoManager()


            
    