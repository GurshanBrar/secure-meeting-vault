from django.db import models

# Create your models here.


class Group(models.Model):
    group_id = models.SlugField(max_length=7, blank=False)
    meeting_url = models.URLField(
        verbose_name='Meeting Link', blank=False, help_text="Enter the meeting link")


class Member(models.Model):
    name = models.CharField(max_length=200, blank=False)
    encoded_file = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
