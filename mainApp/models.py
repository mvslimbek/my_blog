from django.db import models
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    datetime = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        unique_slug = self.slug
        num = 1
        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{self.slug}-{num}'
            num += 1
        self.slug = unique_slug
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Talks(models.Model):
    title = models.CharField(max_length=255)
    photo = models.URLField()
    datetime = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title
