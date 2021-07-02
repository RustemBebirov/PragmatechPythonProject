from typing import Callable
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()



# Create your models here.



# Blog model start

class Tag(models.Model):
    """this table show  tag information"""

    # information's
    title = models.CharField('Title',max_length=127,)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('title','-created_at')
    
    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    """this table show blog information"""

    # relation's
    category = models.ForeignKey('Blog_category', on_delete=models.CASCADE, related_name='blogs', db_index=True)


    # information's
    title = models.CharField('Title',max_length=127,)
    short_description = models.CharField('Short description', max_length=127 )
    description = models.TextField("Description", null=True)
    image = models.ImageField("Image", upload_to='blog_images')
    slug = models.SlugField('Slug',max_length=160,)
    tag = models.ManyToManyField(Tag, verbose_name='Tag')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)



    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('title','-created_at')
         

    def __str__(self) -> str:
        return self.title




class Blog_category(models.Model):
    """this table show blog category information"""

    # information's
    title = models.CharField('Title',max_length=127,)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title','-created_at')
         

    def __str__(self) -> str:
        return self.title




class Blog_comment(models.Model):
    """ in this table you can store comment information"""

    # relation's
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True, related_name='comments')
    parrent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=CASCADE, db_index=True, related_name='sub_comment')
    blog = models.ForeignKey('Blog', verbose_name='Blog', related_name='blogs',db_index=True, on_delete=CASCADE)


    # information's
    content = models.TextField("Content",)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.author.get_full_name()}'

# Blog model end


# Order model start
class Order(models.Model):
    """this table show order information"""

    # information's
    title = models.CharField('Title',max_length=127)
    price = models.CharField('Price',max_length=127)
    short_description = models.CharField('Short Description',max_length=127)
    description = models.TextField('Description')
    seller = models.CharField('Seller',max_length=127)
    image1 = models.ImageField("Image", upload_to='shop_images')
    image2 = models.ImageField("Image", upload_to='shop_images')
    image3 = models.ImageField("Image", upload_to='shop_images')
    image4 = models.ImageField("Image", upload_to='shop_images')
    image5 = models.ImageField("Image", upload_to='shop_images')

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

class Order_Comment(models.Model):

    # relation's
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True, related_name='comments')
    order = models.ForeignKey('Order', verbose_name='Order', related_name='orders',db_index=True, on_delete=CASCADE)
    
    
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
        return self.full_name

# ORder model end

# Teacher model start
class Teacher(models.Model):
    # relation's
    
    """this table show Order comment information"""
    full_name = models.CharField("FullName",max_length=127)
    job = models.CharField('Job',max_length=127)
    short_description = models.CharField("Short description",max_length=127)
    about = models.CharField("About",max_length=127)
    acchivments = models.CharField("Achivments",max_length=127)
    objective = models.CharField("My Objective" ,max_length=127)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return self.full_name
    
class Teacher_Comment(models.Model):
    # relation's
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True, related_name='comments')
    teacher = models.ForeignKey('Teacher', verbose_name='Teacher', related_name='teachers',db_index=True, on_delete=CASCADE)
    
    
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
        verbose_name = 'Teacher Comment'
        verbose_name_plural = 'Teacher Commnets'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return self.full_name
# Teacher model end

# Course model start
class Course(models.Model):
    # relation's
    teacher = models.ForeignKey('Teacher', verbose_name='Teacher', related_name='teachers',db_index=True, on_delete=CASCADE)
    category = models.ForeignKey('Course_category', on_delete=models.CASCADE, related_name='courses', db_index=True)
    
    """this table show Order comment information"""
    title = models.CharField('FullName',max_length=127)
    rating = models.IntegerField("Rating")
    price = models.CharField("Price", max_length=127)
    

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Teacher Comment'
        verbose_name_plural = 'Teacher Commnets'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return self.full_name

    class Course_category(models.Model):
        """this table show Course category information"""

        # information's
        title = models.CharField('Title',max_length=127,)

        # moderation's
        created_at = models.DateField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)
        is_published = models.BooleanField('Is published', default=True)

        class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'
            ordering = ('title','-created_at')
            

        def __str__(self) -> str:
            return self.title


# Course model end


class Contact(models.Model):
    """this table show category information"""


    # information's
    full_name = models.CharField('FullName',max_length=127)
    email = models.EmailField('E-mail',max_length=127)
    subject = models.CharField('Subject',max_length=127)
    phone = models.IntegerField("Phone",)
    message = models.TextField('Message', help_text='You can send your mesaage from here')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return f'{self.subject} adli feedback'