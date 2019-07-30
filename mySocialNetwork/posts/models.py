from django.db import models
# reverse is for set reverse url after submit
from django.urls import reverse
# 
from django.conf import settings

# Group is imported cz we can connect Post with specific group
from groups.models import Group



# POSTS MODELS.PY FILE
# Create your models here.

# misaka is used to linking with text.
import misaka

# bcz in this project django default authorization model is activated
from django.contrib.auth import get_user_model
# This User object will connect the current post with logged in user
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})
