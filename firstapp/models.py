from typing import Callable
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.urls import reverse

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
         

    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):
        return reverse('firstapp:blog-single',args=([self.slug]))



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
    # parent = models.ForeignKey("self", null=True, blank=True, on_delete=CASCADE)

    # information's
    full_name = models.CharField('FullName',max_length=127)
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
        return f'  {self.blog}  yazilan comment'

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
        return f'{self.full_name} adli sexsin {self.order} adli ordere commenti'


class Order_category(models.Model):
    """this table show order category information"""

    # information's
    title = models.CharField('Title',max_length=127,)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Order Category'
        verbose_name_plural = 'Order Categories'
        ordering = ('title','-created_at')
         

    def __str__(self) -> str:
        return self.title
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
    image = models.ImageField("Image",upload_to='teacher_images')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ('full_name','-created_at')
    
    def __str__(self) -> str:
        return self.full_name

    def get_absolute_url(self):
        return reverse('firstapp:teachers-single',args=([self.id]))
    
class Teacher_Comment(models.Model):
    # relation's
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
        ordering = ('full_name','-created_at')
    
    def __str__(self) -> str:
        return f'{self.full_name} adli sexsin {self.teacher} adli mellime commenti'
# Teacher model end

# Course model start
class Course(models.Model):
    # relation's
    category = models.ForeignKey('Course_category', on_delete=models.CASCADE, related_name='courses', db_index=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course', db_index=True)

    """this table show Order comment information"""
    title = models.CharField('Title',max_length=127)
    price = models.CharField("Price", max_length=127)
    image = models.ImageField("Image",upload_to='course_images')
    summery = models.CharField("Summery", max_length=127)
    requrements = models.CharField("Requrements", max_length=127,blank=True,null=True)
    instructor = models.CharField("Instructor", max_length=127,blank=True,null=True)
    durations = models.CharField("Duration",max_length=127,blank=True,null=True)
    leactures = models.CharField('Leactures',max_length=127)
    quizzes = models.CharField("Quizzes",max_length=127)
    
    

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ('title','-created_at')
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('firstapp:courses-single',args=([self.id]))


class Course_category(models.Model):

    """this table show Course category information"""

    # information's
    title = models.CharField('Title',max_length=127,)

     # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Curse Category'
        verbose_name_plural = 'Curse Categories'
        ordering = ('title','-created_at')
            

    def __str__(self) -> str:
        return self.title


    """this table show  tag information"""

    # information's
    lecture = models.CharField('Lecture',max_length=127,)
    title = models.CharField('Title',max_length=127,)
    time = models.CharField('Course time',max_length=127,)
    short_description = models.CharField('Short Description',max_length=127,)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Curriculum'
        verbose_name_plural = 'Curriculums'
        ordering = ('title','-created_at')
    
    def __str__(self) -> str:
        return self.title

   

class Course_Comment(models.Model):
    """this table show Course comment information"""
    
    # relation's
    course = models.ForeignKey('Course', verbose_name='Course', related_name='comment',db_index=True, on_delete=CASCADE)
    
    # information's
    full_name = models.CharField('FullName',max_length=127)
    email = models.EmailField("E-mail",max_length=127)
    rating = models.IntegerField("Rating")
    comment = models.TextField('Comment')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Course comment'
        verbose_name_plural = 'Courses comments'
        ordering = ('-created_at',)
    
    def __str__(self) -> str:
        return f'{self.full_name} adli sexsin {self.course} adli kursa commenti'
    
   


# Course model end

# Event model start
class Event(models.Model):
    """this table show you event information"""
     # relation's
    teacher = models.ForeignKey('Teacher', verbose_name='Teacher', related_name='event',db_index=True, on_delete=CASCADE)

    # information's
    title = models.CharField('Title',max_length=127)
    start = models.DateTimeField('Start time')
    end = models.DateTimeField("End time")
    auditor = models.CharField("Auditor",max_length=127)
    short_description = models.CharField('Short Description',max_length=127)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='Event images')
    singleimage = models.ImageField('Single Image', upload_to='Event images')
    address = models.CharField("Address",max_length=127)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)


    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ('title','-created_at')

    def __str__(self) -> str:
        return f'{self.title} adli event'    

    def get_absolute_url(self):
        return reverse('firstapp:events-single',args=([self.id]))
    
class Contact(models.Model):
    """this table show contact information"""


    # information's
    full_name = models.CharField('FullName',max_length=127)
    email = models.EmailField('E-mail',max_length=127)
    subject = models.CharField('Subject',max_length=127)
    phone = models.CharField("Phone",max_length=127)
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