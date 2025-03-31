from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def str(self):
        return f'{self.first_name} - {self.last_name}'



class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.follower} - {self.following}'


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    post_image = models.ImageField(upload_to='post_image', null=True, blank=True)
    post_video = models.FileField(upload_to='post_video/', null=True, blank=True)
    description = models.TextField()
    hashtag = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user} - {self.post_image} - {self.post_video}'


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post',)

    def str(self):
        return f'{self.user}, {self.post} - {self.like}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user}, {self.text}'


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user}, {self.like}'


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    story_image = models.ImageField(upload_to='story_image', null=True, blank=True)
    story_video = models.FileField(upload_to='story_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.user} - {self.story_image} - {self.story_video}'


class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_saved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.post}'

class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    create_date = models.DateField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)