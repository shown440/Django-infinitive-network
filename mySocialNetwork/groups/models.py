from django.db import models

# slugify helps us to remove spaces and various character. BCZ in URL we can't use any spaces, upper case
    # and various characters.   
from django.utils.text import slugify
# reverse is for set reverse url after submit
from django.urls import reverse


# GROUPS MODELS.PY FILE
# Create your models here.

# misaka is used to linking with text.
import misaka

# bcz in this project django default authorization model is activated
from django.contrib.auth import get_user_model
# This User object will connect the current post with logged in user
User = get_user_model()

from django import template
register = template.Library()



class Group(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']



class GroupMember(models.Model):

    group = models.ForeignKey(Group, related_name='membership', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_group', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')

