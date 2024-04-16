from django.db import models

# Create your models here.


class Category(models.Model):
    """For category fields"""

    name = models.CharField(max_length=50, unique=True, verbose_name="Category name")
    published = models.BooleanField(default=True, verbose_name="Is published")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated time")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"


class Recipe(models.Model):
    """For recipe fields"""

    name = models.CharField(max_length=255, verbose_name="Recipe name")
    content = models.TextField(blank=True, null=True, verbose_name="Recipe content")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
    updated = models.DateTimeField(auto_now=True, verbose_name="updated time")
    published = models.BooleanField(default=True, verbose_name="Is published")
    views_count = models.IntegerField(default=0, verbose_name="Views count")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    class Meta:
        ordering = ["-pk"]




