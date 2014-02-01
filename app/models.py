from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class DogeUser(AbstractBaseUser,PermissionsMixin):
    nickname = models.CharField(max_length=100,blank = False,unique = False)
    name = models.CharField(max_length=100,blank = False)
    email = models.EmailField(max_length = 254, unique = True)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(default = timezone.now)
    is_manager = models.BooleanField(default = False)
    facebook_id = models.BigIntegerField(blank = False, unique = True)
    
    
    def _unicode_(self):
        return self.
    
    def _get_full_name(self):
        return "%s" % (self.name)
    
    class Meta:
        ordering = ('facebook_id',)

class DogeManager(BaseUserManager):
    def _create_user(self,email,is_manager,name,
        facebook_id):
    
        now = timezone.now()
        email = normalize_email(email)
    
        user = self.model(nickname = nickname, email = email, 
                    is_manager = is_manager,name,is_active = True,
                    date_joined = now, facebook_id = facebook_id)
        user.save()
        return user
    
    def create_user(self,nickname,email,name,facebook_id):
        return self._create_user(email, False,name,facebook_id)

    def create_superuser(self,nickname,email,name,facebook_id):
        return self._create_user(email, True,name,facebook_id)        
        
class Friendship(models.Model):
    user = models.OneToOneField(DogeUser)
    friends = models.ManyToManyField('self',symmetrical = True)
    
    class Meta:
        verbose_name = _(u'friendship')
        verbose_name_plural = _(u'friendships')
        
    objects = FriendMan
        
    def _unicode_(self):
        return _(u'%(user)s\'s friends') % {'user': unicode(self.user)}
    
    def friend_count(self):
        return self.friends.count()
    
class FriendReq(models.Model):
    
    from_user = models.ForeignKey(DogeUser)
    to_user = models.ForeignKey(DogeUser)
    created = models.DateTimeField(default = datetime.datetime.now)
    accepted = models.BooleanField(default = False)
    
    def _unicode_(self):
        return _(u'%(from_user)s wants to be friends with $(to_user)s') % 
                {'from_user': unicode(self.from_user),
                 'to_user': unicode(self.to_user),}
        
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
        return DogeUser.objects.filter(friendship_friends_user = user)
    
    def are_friends(self,user1,user2):
        friendship = Friendship.objects.get(user=user1)
        return bool(friendship.friends.filter(user=user2).exists())
    
    def befriend(self,user1,user2):
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.add(Friendship.objects.get(user=user2))
        FriendshipRequest.objects.filter(from_user=user1,to_user=user2).delete()
    
    def unfriend(self,user1,user2):
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.remove(Friendship.objects.get(user=user2))
        FriendshipRequest.objects.filter(from_user=user1,to_user=user2).delete()
        FriendshipRequest.objects.filter(from_user=user2,to_user=user1).delete()        
        