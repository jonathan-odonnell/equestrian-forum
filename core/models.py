from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.text import slugify


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    category = models.ForeignKey(
        Category, null=True, blank=True,
        on_delete=SET_NULL, related_name='posts')
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        """
        Override the original save method to generate the slug.
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return f'Image {self.id} on post {self.post.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment {self.id} on post {self.post.title}'
