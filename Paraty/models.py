from django.db import models
from django.contrib.auth.models import User

class UserConnection(models.Model):
    user_from = models.ForeignKey(User, related_name='connections', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='connected_to', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_from', 'user_to')

