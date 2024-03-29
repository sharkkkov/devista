from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to="images/")

    def __str__(self):
        return self.post.title


class Reference(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title