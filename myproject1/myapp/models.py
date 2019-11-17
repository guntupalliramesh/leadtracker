from django.db import models

# Create your models here.

class Register(models.Model):
	NAME = models.CharField(max_length = 25)
	MOBILE = models.CharField(max_length = 25)
	EMAIL = models.CharField(max_length = 25)
	COURSE = models.CharField(max_length = 25)
	SOURCE= models.CharField(max_length = 25)
	LEAD_STATUS= models.CharField(max_length = 25)
	DEMO_DATE = models.CharField(max_length = 25)
	COUNSIER = models.CharField(max_length = 25)
	REMARKS = models.CharField(max_length = 25)


	def __str__(self):
		return self.NAME


class demo(models.Model):
	NAME = models.CharField(max_length = 25)
	COURSE = models.CharField(max_length = 25)
	DATE_OF_JOINNING= models.CharField(max_length = 25)
	DATE_OF_COMPLETION= models.CharField(max_length = 25)
	COURSE_FEE= models.CharField(max_length = 25)
	INSTRUCTOR = models.CharField(max_length = 25)
	AADHAR_NO = models.CharField(max_length = 25)
	MOBILE_NO = models.CharField(max_length = 25)
	EMAIL = models.CharField(max_length = 25)
	REMARKS = models.CharField(max_length = 25)
	status = models.CharField(max_length=20)

	def __str__(self):
		return self.NAME