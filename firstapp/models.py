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

    # moderaiton's
    created_ad = models.DateField(auto_now_add=True)
    updated_ad = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'
         


    # def get_category_display(self):
    #     return self.category

    def __str__(self) -> str:
        return self.title

    