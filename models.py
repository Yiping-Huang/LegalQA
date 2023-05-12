from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """the topic of a legal question"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return the string representation of the model"""
        return self.text


class Description(models.Model):
    """the description of a legal question"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'descriptions'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


class Reply(models.Model):
    """the reply of a legal question."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'replies'
        # Create view consultations permission instance manually in poc_permission_required  view function
        permissions = (
            ('edit_replies', 'Can add and edit replies'),
        )

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."


class Comment(models.Model):
    """the comment of a legal question's reply."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."

