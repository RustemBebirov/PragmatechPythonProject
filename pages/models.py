from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField('Title',max_length=50)
    image = models.ImageField('Image',upload_to='gallery_images')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        ordering = ('title','-created_at')


    def __str__(self) -> str:
        return self.title