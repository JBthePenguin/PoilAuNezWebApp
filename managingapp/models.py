from django.contrib.auth.models import AbstractUser


class Manager(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email
