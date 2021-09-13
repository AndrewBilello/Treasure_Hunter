from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        email_taken = User.objects.filter(email = post_data["email"])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 1:
            errors['first_name'] = "First name required"
        if len(post_data['last_name']) < 1:
            errors['last_name'] = "Last name required"
        if len(post_data['email'])== 0:
            errors['email'] = "Email required"
        if len(post_data['password']) < 5:
            errors['password'] = "Password must be more than 5 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['match']= "Passwords do not match"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Email address does not use valid characters"
        elif len(email_taken) > 0:
            errors['email_taken'] = "That email is already registered"
        return errors

    def login_validator(self, post_data):
        errors = {}
        existing_user = User.objects.filter(email = post_data['email'])
        if len(post_data['email'])== 0:
            errors['email'] = "Email required"
        if len(existing_user)== 0:
            errors['does_not_exist']= "Please enter a valid email and password"
        if len(post_data['password'])== 0:
            errors['password'] = "Password required"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

