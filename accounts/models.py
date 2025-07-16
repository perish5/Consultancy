from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ROLES = (
        ("admin", "Admin"),
        ("user", "User")
        )
    role = models.CharField(max_length=50, choices=ROLES, default="student")
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True,)
    contact_num = models.CharField(max_length=15, null=True, default=True)
    address = models.CharField(max_length=255, null=False, default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "role", "first_name", "last_name"
    
    def __str__(self):
        return self.username 
    
