from django.db import models
#
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey

from versatileimagefield.fields import VersatileImageField

def upload_to(instance, filename):
    try:
        title = instance.post.title
    except:
        title = instance.title
    slug = slugify(title)
    return 'posts/{filename}'.format(filename = slug + '_' + filename)


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=800, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    creation_date = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = VersatileImageField('Mainimage',upload_to=upload_to)
    

    def __str__(self):
        return self.post.title
