from django.db import models

# Create your models here.
class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False) # not null auto_increment primary key
    gender = models.CharField(max_length=55, blank=False) #varchar(55) not null
    date_created = models.DateTimeField(auto_now_add=True) #timestamp default current_timestamp
    date_updated = models.DateTimeField(auto_now=True) #timestamp default current_timestamp on update current_timestamp

    class Meta:
        db_table = 'genders'

    def __str__(self):
        return self.gender    

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)  
    last_name = models.CharField(max_length=55, blank=False)      
    age = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55, blank=False)
    password = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True) #timestamp default current_timestamp
    date_updated = models.DateTimeField(auto_now=True) #timestamp default current_timestamp on update current_timestamp

    class Meta:
        db_table = 'users'

