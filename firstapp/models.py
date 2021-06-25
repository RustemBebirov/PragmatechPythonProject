from django.db import models

# Create your models here.

class Blog(models.Model):
    """in this table blog information"""

    Blog_categories = (
        (1,'Travel'),
        (2,'Food')
    )

    title = models.CharField('Bashliq',max_length=127,)
    short_description = models.TextField('Qisa mezmun', blank=True )
    description = models.TextField("Mezmun", null=True)
    image = models.ImageField("Shekil", upload_to='blog_image')
    category = models.IntegerField('Kategory', choices=Blog_categories )
