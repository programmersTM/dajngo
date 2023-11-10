from django.db import models
from django.conf import settings


class Blog(models.Model):
    CHOISE = [
        ('pub', 'published'),
        ('drf', 'Draft',)
    ]

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    published = models.CharField(default='pub', max_length=3, choices=CHOISE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post