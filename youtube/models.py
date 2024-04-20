import datetime

from django.db import models, transaction


class Video(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    publish_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()
    video_id = models.CharField(max_length=150, unique=True)
    channel_id = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ', '.join(['title=' + self.title, 'description=' + self.description])


class APIAuthKey(models.Model):
    auth_key = models.CharField(max_length=250, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    exhausted = models.BooleanField(default=False)

    @classmethod
    def get_auth_key(cls):
        """
        Returns the non-exhausted API auth key.
        The newest auth key is returned.
        """
        with transaction.atomic():
            auth_key_object = cls.objects.select_for_update(skip_locked=True).filter(exhausted=False).order_by('-created').first()
            if auth_key_object:
                return auth_key_object.auth_key
        return None

    @classmethod
    def mark_auth_key_exhausted(cls, auth_key):
        """
        Marks the API auth key as exhausted.
        """
        with transaction.atomic():
            auth_key_object = cls.objects.select_for_update().get(auth_key=auth_key)
            auth_key_object.exhausted = True
            auth_key_object.save()
        return auth_key_object
