from django.db import models

# Create your models here.
class login_table(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class doctor_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.FileField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    post = models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class user_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email = models.CharField(max_length=100)

class feedback_table(models.Model):
    USER = models.ForeignKey(user_table,on_delete=models.CASCADE)
    DOCTOR = models.ForeignKey(doctor_table,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    date = models.DateField()

class complaint_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    DOCTOR = models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.DateField()




class schedule_table(models.Model):
    DOCTOR = models.ForeignKey(doctor_table, on_delete=models.CASCADE)
    from_Date = models.DateField()
    to_Date=models.DateField()
    foom_time = models.TimeField()
    to_time = models.TimeField()
    days=models.CharField(max_length=100)


class booking_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    SCHEDULE = models.ForeignKey(schedule_table, on_delete=models.CASCADE)
    # slot = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100)

class report_table(models.Model):
    booking = models.ForeignKey(booking_table, on_delete=models.CASCADE)
    report_typr = models.CharField(max_length=200)
    date = models.DateField()
    report = models.FileField()

#class prediction_table(models.Model):
 #   USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
  #  image=models.FileField()

