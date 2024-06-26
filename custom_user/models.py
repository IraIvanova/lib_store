from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class Plan(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    desc = models.TextField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    email = models.EmailField('Email address', unique=True)
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    learned_language = models.CharField(max_length=10, default='English')
    interface_language = models.CharField(max_length=10, default='Ukrainian')
    image = models.CharField(null=True, blank=True)
    email_is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
