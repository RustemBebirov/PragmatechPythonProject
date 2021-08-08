from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.contrib.auth import get_user_model

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
    blog_author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blogauthor', db_index=True)

    # information's
    title = models.CharField('Title',max_length=127,)
    short_description = models.CharField('Short description', max_length=127 )
    description = models.TextField("Description", null=True)
    image = models.ImageField("Image", upload_to='blog_images')
    slug = models.SlugField('Slug',max_length=160,unique_for_date='created_at')
    tag = models.ManyToManyField(Tag, verbose_name='Tag',related_name='blogs')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)



    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('title','-created_at')
         
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):
        return reverse('blogs:blog-single',args=([self.slug]))



class Blog_category(models.Model):
    """this table show blog category information"""

    # information's
    title = models.CharField('Title',max_length=127,)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'
        ordering = ('title','-created_at')
         

    def __str__(self) -> str:
        return self.title




class Blog_comment(models.Model):
    """ in this table you can store comment information"""

    # relation's
    # author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True, related_name='comments')
    blog = models.ForeignKey('Blog', verbose_name='Blog', related_name='comment_blog',db_index=True, on_delete=CASCADE)
    # parent = models.ForeignKey("self", null=True, blank=True, on_delete=CASCADE,related_name='reply')

    # information's
    author = models.CharField('FullName',max_length=127)
    email = models.EmailField("E-mail",max_length=127)
    content = models.TextField("Content",)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'  {self.blog}  {self.author} terefinden   yazilan comment'

    def get_absolute_url(self):
        return reverse('blogs:blog_comment_reply',args=([self.id]))


class Blog_comment_reply(models.Model):
    """ in this table you can show comment reply information"""
    comment = models.ForeignKey(Blog_comment,on_delete=models.CASCADE,related_name='replies')
   
    # information's 
    author = models.CharField('FullName',max_length=127)
    email = models.EmailField("E-mail",max_length=127)
    content = models.TextField("Content",)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Comment reply'
        verbose_name_plural = 'Blog Comments reply' 
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'  {self.comment} e {self.content}  yazilan comment'

# Blog model end