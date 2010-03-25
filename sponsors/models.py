from django.db import models

class Sponsors(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from name. Must be unique.")
    url = models.URLField(default="http://",
                          help_text="URL to website")
    address = models.TextField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    logo = models.ImageField(upload_to="sponsors/logos", blank=True, null=True)
    discount_detail = models.TextField()
    
    class Meta:
        verbose_name_plural = "Sponsors"
    
    def __unicode__(self):
        return self.name