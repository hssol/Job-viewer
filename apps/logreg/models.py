from django.db import models
import bcrypt

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        user_result = User.objects.filter(username=postData['login_username'])
        if not user_result:
            errors["user"] = "Username and password are invalid"
            return errors
    
        hashed_password = user_result[0].password
        password = postData['login_password']
        if not bcrypt.checkpw(password.encode(), hashed_password.encode()):
            errors["password"] = "Username and password are invalid"
            return errors
        
        else:
            return errors

    def register_validator(self, postData):
        errors = {}
        if len(postData['register_username']) < 3:
            errors['register_username'] = "Username must be more than 3 characters"
        if len(postData['register_email']) < 3:
            errors['register_email'] = "email must be more than 7 characters"
        if len(postData['register_password']) < 6:
            errors['register_password'] = "Password must be more than 6 characters"
        return errors



class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

