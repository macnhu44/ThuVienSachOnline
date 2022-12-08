from django.db import models

# Create your models here.
class Customer (models.Model):
    GENDER = [(1, "Nam"), (0, "Nữ")]
    
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=100, null=True, choices=GENDER, default=1)
    
    def __str__(self):
        return self.name
    
class Book (models.Model):
    CATEGORY = [('Sách Giáo Khoa', 'Sách Giáo Khoa'),
                ('Tiểu Thuyết', 'Tiểu Thuyết'),
                ('Truyện Tranh', 'Truyện Tranh')]
    
    name = models.CharField(max_length=200, null=True, blank=False)
    author = models.CharField(max_length=200, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATEGORY, default='sgk')
    release_date = models.DateTimeField(max_length=200, null=False, blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name