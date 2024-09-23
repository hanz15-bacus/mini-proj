from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} on {self.post.title}'

from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    username = models.CharField(max_length=254, unique=True)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)  # Increased length to accommodate hashed passwords

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        """Hashes the password using Django's password hashing system."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Verifies the password against the stored hash."""
        return check_password(raw_password, self.password)

    