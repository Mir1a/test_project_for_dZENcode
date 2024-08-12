from django.db import models
from django.utils import timezone


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    homepage = models.URLField(blank=True, null=True)
    captcha = models.ImageField(upload_to='captcha_images/')
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    user = models.ForeignKey(
        to="users.User",
        on_delete=models.SET_NULL,
        related_name='comments',
        blank=True,
        null=True,)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='replies',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Comment by {self.user_name}'
