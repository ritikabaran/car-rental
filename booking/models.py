from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=10,null=False)
    name=models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    fathers_name=models.CharField(max_length=30,default='')
    mothers_name=models.CharField(max_length=30,default='')
    phone=models.CharField(max_length=10,default='')
    email=models.CharField(max_length=30,default='')
    address=models.CharField(max_length=50,default='')
    def __str__(self):
        return self.username
    
class from_to(models.Model):
    book_from=models.CharField(max_length=30)
    book_to=models.CharField(max_length=30)
    km=models.IntegerField(default=0)
    date=models.CharField(max_length=30)
    car=models.CharField(max_length=30)

class bookHistory(models.Model):
    book_id=models.CharField(max_length=30,primary_key=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    book_from=models.CharField(max_length=30)
    book_to=models.CharField(max_length=30)
    car=models.CharField(max_length=30)
    price=models.IntegerField()

class carPrice(models.Model):
    car=models.CharField(max_length=30,primary_key=True)
    perKmPrice=models.IntegerField()