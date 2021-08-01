from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()
# Create your models here.

# Teacher model start
class TeacherInfo(models.Model):

    # relation's
    user = models.ForeignKey(User, verbose_name='User', related_name='infos',db_index=True, on_delete=models.CASCADE)
    
    
    
    """this table show Teacher Infos  information"""
    job = models.CharField('Job',max_length=127,null=True)
    short_description = models.CharField("Short description",max_length=127,null=True)
    about = models.CharField("About",max_length=127,null=True)
    acchivments = models.CharField("Achivments",max_length=127,null=True)
    objective = models.CharField("My Objective" ,max_length=127,null=True)
    image = models.ImageField("Info Image 270x308", upload_to='teacherinfo_image')

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField('Is published', default=True)

    class Meta:
        verbose_name = 'Teacher Info'
        verbose_name_plural = 'Teachers Infos'
        ordering = ('user','-created_at')
    
    def __str__(self) -> str:
        return self.user.fullname

    # def get_absolute_url(self):
    #     return reverse('teachers:teachers-single',args=([self.id]))
    
class Teacher_Comment(models.Model):
    # relation's
    teacher = models.ForeignKey(User, verbose_name='Teacher', related_name='teachers',db_index=True, on_delete=models.CASCADE)
    
    
    """this table show Teacher comment information"""
    fullname = models.CharField('FullName',max_length=127)
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
        ordering = ('fullname','-created_at')
    
    def __str__(self) -> str:
        return f'{self.fullname} adli sexsin {self.teacher} adli mellime commenti'
# Teacher model end




# Course model start
class Course(models.Model):

    # relation's
    category = models.ForeignKey('Course_category', on_delete=models.CASCADE, related_name='courses', db_index=True)
    curriculum = models.ManyToManyField('Curriculum',related_name='curriculum', db_index=True)
    user = models.ForeignKey(User, verbose_name='User', related_name='courses',db_index=True, on_delete=models.CASCADE)

    """this table show Course comment information"""
    title = models.CharField('Title',max_length=127)
    price = models.CharField("Price", max_length=127)
    sale = models.CharField("Sale Price",max_length=127,blank=True,null=True)
    image = models.ImageField("Image 369x251 ",upload_to='course_images')
    summery = models.CharField("Summery", max_length=127)
    requrements = models.CharField("Requrements", max_length=127,blank=True,null=True)
    durations = models.IntegerField(verbose_name="Quizzes",blank=True,null=True)
    leactures = models.IntegerField(verbose_name='Leactures',blank=True,null=True)
    quizzes = models.IntegerField(verbose_name="Quizzes",blank=True,null=True)
    
    

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
        return reverse('teachers:courses-single',args=([self.id]))


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


class Curriculum(models.Model):

    """this table show Curriculum comment information"""
    title = models.CharField('Title',max_length=127)
    short_description = models.CharField("Short Description", max_length=127)
    lecture = models.FloatField('Lecture',blank=True)
    time = models.FloatField("Lecture time",blank=True)

    # moderation's
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Curriculum'
        verbose_name_plural = 'Curriculums'
        ordering = ('title','-created_at')

    def __str__(self) -> str:
        return self.title


# Course model end

# Event model start
class Event(models.Model):
    """this table show you event information"""
     # relation's
    teacher = models.ForeignKey(User, verbose_name='Teacher', related_name='event',db_index=True, on_delete=models.CASCADE)

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
        return reverse('teachers:events-single',args=([self.id]))

