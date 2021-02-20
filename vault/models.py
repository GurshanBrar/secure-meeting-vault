from django.db import models

# Create your models here.


class Group(models.Model):
    group_id = Models.SlugField(max_length=7, blank=False)
    meeting_url = Models.URLField(
        verbose_name='Meeting Link', blank=true, help_text="Enter the meeting link")


class Member(models.Model):
    name = Models.CharField(max_length=200)
    encoded_file = Models.TextField()
    group = models.ForeignKey(Group, on_delete=Models.CASCADE)
