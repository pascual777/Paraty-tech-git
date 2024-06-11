from django.db import models


class UserConnection(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='connections', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User', related_name='connected_to', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_from} connects to {self.user_to}"


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
