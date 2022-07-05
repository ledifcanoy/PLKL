from django.db import models

class FilmRequest (models.Model):
	cphile_name = models.CharField(max_length=100, blank=True)
	cphile_email = models.CharField(max_length=100, blank=True)
	cphile_title = models.CharField(max_length=100, blank=True)
	cphile_director = models.CharField(max_length=100, blank=True)
	cphile_genre = models.CharField(max_length=100, blank=True)

class Branch(models.Model):
	itemcountry = models.CharField(max_length=100, blank=True)
	itemcity = models.CharField(max_length=100, blank=True)
	itemcinema =models.CharField(max_length=100, blank=True)
	itemgate = models.CharField(max_length=100, blank=True)

class Show(models.Model):	
	itemmovie = models.CharField(max_length=100, blank=True)
	itemdate = models.CharField(blank = True, max_length=100,)
	itemtime = models.CharField(blank = True, max_length=100,)
	itemtickets = models.CharField(max_length=100, blank=True)
	itemdateres = models.DateField( blank=True)
	itemtimeres = models.TimeField(blank = True)

class CustomerInformation (models.Model):	
	itemname = models.CharField(max_length=100, blank=True)
	itememail = models.CharField(max_length=100, blank=True)
	itemmobile = models.CharField(max_length=100, blank=True)
	itempayment = models.CharField(max_length=100, blank=True)
	itemwallet = models.CharField(max_length=100, blank=True)