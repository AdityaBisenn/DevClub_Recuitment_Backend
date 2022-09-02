from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.




class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Sport(models.Model):
    name = models.CharField(max_length=100)

class Court(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()


class Slot(models.Model):
    court = models.ForeignKey(Court,on_delete=models.CASCADE)
    booked = models.IntegerField(default=0)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status1 = (('1','available'),('2','booked'),('3','cancelled'))

    status = models.CharField(max_length=1,choices=status1,default='1')

    # members = models.ManyToManyField(Member)

    def __str__(self):
        return str(self.date) + " " + str(self.start_time) +" - "+ str(self.end_time)


class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    entry_num = models.CharField(max_length=100)
    slots = models.ManyToManyField(Slot,blank=True)

    # if booked>=capacity:
    #     status = '2'

    

# class Sport(models.Model):



