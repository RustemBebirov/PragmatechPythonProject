from django.db import models


# Create your models here.


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