from __future__ import unicode_literals

from profile import Profile

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Cafe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    main_image_url = models.URLField()

    def __str__(self):
        return self.name


class CafeImage(models.Model):
    cafe = models.ForeignKey(to=Cafe, related_name='all_images')
    image_url = models.URLField()


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


        # class Member(models.Model):
        #
        #     name = models.CharField(max_length=30)
        #     record = models.CharField(max_length=200, blank=True, null=True)
        #     pub_date = models.DateTimeField('date', blank=True, null=True)
        #
        #
        # class Data(models.Model):
        #
        #     member = models.ForeignKey(Member)
        #     dob = models.CharField(max_length=200, blank=True, null=True)
        #     event = models.CharField(max_length=200, blank=True, null=True)
        #     description = models.CharField(max_length=200, blank=True, null=True)
        #     gender = models.CharField(max_length=200, blank=True, null=True)
        #
        #     def save(self, *args, **kwargs):
        #
        #         member, _ = Member.objects.get_or_create(name = self.name)
        #         # can update member here with other fields that relate to them
        #         self.member = member
        #         super(Data, self).save(*args, **kwargs)
