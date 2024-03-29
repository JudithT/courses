from __future__ import unicode_literals

from django.db import models

class Coursename(models.Model):
    course_name = models.CharField(max_length = 255)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
