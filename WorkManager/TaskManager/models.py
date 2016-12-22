from django.db import models

# Create your models here.
class UserProfile(models.Model):
	name = models.CharField(max_length=50, verbose_name="Name")
	login = models.CharField(max_length=25, verbose_name="Login")
	password = models.CharField(max_length=50, verbose_name="Name")
	phone = models.DateField(max_length=20, verbose_name="Phone number", null=True,default=None,blank=True)
	bdate = models.DateField(verbose_name="Birthdate",null=True,default=None,blank=True)
	last_connection = models.DateTimeField(verbose_name="Date last connected",null=True,default=None,blank=True)
	email = models.EmailField(verbose_name="Email")
	years_seniority = models.IntegerField(verbose_name="Seniority",default=0)
	date_created = models.DateField(verbose_name="Create date",auto_now_add=True)