from django.db import models

class file(models.Model): 
	file_id = models.AutoField(primary_key = True)
	file_name = models.CharField(max_length=100, blank = True, null =True)
	file = models.FileField(upload_to='files', blank=True)
	