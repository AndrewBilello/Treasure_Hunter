from django.db import models
from Accounts.models import User

class TreasureManager(models.Manager):
    def treasure_validator(self, post_data, files):
        errors = {}
        if len(post_data['name']) < 1:
            errors['name'] = "Your Treasure needs a name!"
        if len(post_data['description']) < 3:
            errors['description'] = "Description must be at least 3 characters"
        if len(post_data['location']) < 3:
            errors['location'] = "Location must be at least 3 characters"
        if len(post_data['map_url']) < 1:
            errors['map_url'] = "Treasure needs a map"
        if 'image' not in files:
            errors['image'] = "No image uploaded"
        return errors

class Treasure(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(null =True, blank=True, upload_to='images/')
    map_url = models.URLField(max_length=255, null =True, blank=True)
    created_by = models.ForeignKey(User, related_name="treasures_created", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TreasureManager()

    def __str__(self):
        return self.name

class PostManager(models.Manager):
    def post_validator(self, post_data):
        errors = {}
        if len(post_data['post_content']) < 1:
            errors['post_content'] = "Posts cannot be left blank"
        return errors


class Post(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="posts_created", on_delete = models.CASCADE)
    treasure = models.ForeignKey(Treasure, related_name="has_posts", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class CommentManager(models.Manager):
    def comment_validator(self, post_data):
        errors = {}
        if len(post_data['create_comment']) < 1:
            errors['create_comment'] = "Comment cannot be left blank"
        return errors

class Comment(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="comments_created", on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name="has_comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

class HintManager(models.Manager):
    def hint_validator(self, post_data):
        errors = {}
        if len(post_data['hint_content']) < 1:
            errors['hint_content'] = "Hint cannot be left blank"
        return errors

class Hint(models.Model):
    content = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="hints_created", on_delete = models.CASCADE)
    treasure = models.ForeignKey(Treasure, related_name="has_hints", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = HintManager()