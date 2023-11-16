from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=50,
                            blank=True, null=True)
    email = models.EmailField(max_length=50,
                              blank=True, null=True)
    username = models.CharField(max_length=50,
                                blank=True, null=True)
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
    created = models.DateTimeField(auto_now_add=True)

    # follows = models.ManyToManyField(
    #     'self', related_name='followed_by',
    #     symmetrical=False, blank=True
    # )
    # In the future, we must realize class Interest (ManyToMany)
    class Meta:
        ordering = ['created']
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(Owner,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,
                                blank=True, null=True)
    # Add this atribute to Owner
    city = models.CharField(max_length=20,
                            blank=True, null=True)

    # Need to realized custom class AgeField ex. (4y. 10m.)
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
    parent_1 = models.ForeignKey('Profile',
                                 on_delete=models.CASCADE, blank=True)
    parent_2 = models.ForeignKey('Profile',
                                 on_delete=models.CASCADE, blank=True)

    # In the future, we must realize class Food (favorite foods) and Toy (favorite toys)

    class Meta:
        ordering = ['created']
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return self.user.username
