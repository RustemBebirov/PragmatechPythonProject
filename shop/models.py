from django.db import models

# Create your models here.

class Order(models.Model):
    """this table show order information"""

    # information's
    title = models.CharField('Title',max_length=127)
    price = models.CharField('Price',max_length=127)
    sale = models.CharField('Sale price',max_length=127,blank=True,null=True)
    short_description = models.CharField('Short Description',max_length=127)
    description = models.TextField('Description')
    seller = models.CharField('Seller',max_length=127)
    image =  models.ImageField("Image", upload_to='order_images')
    image1 = models.ImageField("Image", upload_to='order_images')
    image2 = models.ImageField("Image", upload_to='order_images')
    image3 = models.ImageField("Image", upload_to='order_images')
    image4 = models.ImageField("Image", upload_to='order_images')
    image5 = models.ImageField("Image", upload_to='order_images')
    image6 = models.ImageField("Image", upload_to='order_images')
    image7 = models.ImageField("Image", upload_to='order_images')
    image8 = models.ImageField("Image", upload_to='order_images')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('firstapp:shop-single',args=([self.id]))


class Order_Comment(models.Model):

    # relation's
    order = models.ForeignKey('Order', verbose_name='Order', related_name='orders',db_index=True, on_delete=models.CASCADE)
    
    
    """this table show Order comment information"""
    full_name = models.CharField('FullName',max_length=127)
    email = models.EmailField("E-mail",max_length=127)
    rating = models.IntegerField("Rating")
    comment = models.TextField('Comment')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Order comment'
        verbose_name_plural = 'Order comments'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return f'{self.full_name} adli sexsin {self.order} adli ordere commenti'


