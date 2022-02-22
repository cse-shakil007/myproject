from django.db import models

class Update(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    version = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    size = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200, default = False, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Blocked(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    apps = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200, default = False, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.apps

class File(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    file = models.TextField(blank = True)
    status = models.CharField(max_length = 200, default = False, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.file

class VIP(models.Model):
    Active = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    file = models.IntegerField()
    city = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    ip = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    active = models.CharField(max_length = 200, default = False, choices = Active)
    signal = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.city



class Free(models.Model):
    Active = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    file = models.IntegerField()
    city = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    ip = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    active = models.CharField(max_length = 200, default = False, choices = Active)
    signal = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.city

class Data(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    city = models.CharField(max_length = 200)
    vip = models.ManyToManyField(VIP)
    free = models.ManyToManyField(Free)
    status = models.CharField(max_length = 200, default = False, choices = STATUS)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.city

#vip = models.manytoone(VIP, on_delete=models.CASCADE, related_name='vip')
#free = models.ForeignKey(Free, on_delete=models.CASCADE, related_name='free')

