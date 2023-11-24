from django.db import models
from django.contrib.auth.models import AbstractUser
from pytils.translit import slugify
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Owner(AbstractUser):
    phone_number = PhoneNumberField()
    birthday = models.DateTimeField(blank=True, null=True)
    city = models.CharField(max_length=20,
                            blank=True, null=True)
    profession = models.CharField(max_length=50,
                                  blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='profile_images',
        default='profile_images/default.jpg')
    twitter = models.CharField(max_length=100,
                               default='https://twitter.com')
    linkedin = models.CharField(max_length=100,
                                default='https://linkedin.com')
    youtube = models.CharField(max_length=100,
                               default='https://youtube.com')
    website = models.CharField(max_length=100,
                               default='https://mysite.com')
    vk = models.CharField(max_length=100,
                          default='https://vk.com')
    telegram = models.CharField(max_length=100,
                                default='https://tg.com')
    # follows = models.ManyToManyField(
    #     'self', related_name='followed_by',
    #     symmetrical=False, blank=True
    # )
    # In the future, we must realize class Interest (ManyToMany)
    class Meta:
        ordering = ['date_joined']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.ForeignKey(Owner,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,
                                blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)

    # def age(self):
    #     import datetime
    #     return int((datetime.date.today() - self.birthday).days / 365.25)

    city = models.CharField(max_length=20,
                            blank=True, null=True)
    age = models.IntegerField()
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='profile_images',
        default='profile_images/default.jpg')
    twitter = models.CharField(max_length=100,
                               default='https://twitter.com')
    vk = models.CharField(max_length=100,
                          default='https://vk.com')
    telegram = models.CharField(max_length=100,
                                default='https://tg.com')
    created = models.DateTimeField(auto_now_add=True)
    follows = models.ManyToManyField(
        'self', related_name='followed_by',
        symmetrical=False, blank=True
    )
    # parent_1 = models.ForeignKey('Profile',
    #                              on_delete=models.CASCADE, blank=True)
    # parent_2 = models.ForeignKey('Profile',
    #                              on_delete=models.CASCADE, blank=True)

    # In the future, we must realize class Food (favorite foods) and Toy (favorite toys)

    class Meta:
        ordering = ['created']
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return self.user.username


class Interest(models.Model):
    name = models.CharField(max_length=50,
                            blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ManyToManyField(
        Owner, blank=True)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'
        # unique_together = ('name', 'slug', 'profile')

    def __str__(self):
        return self.name
