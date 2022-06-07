from django.shortcuts import render
import requests 
from django.http import JsonResponse
from .models import file
# Create your views here.
def home(request): 
	context = { }
	return render(request, 'html/home.html', context) 

def upload_file(request):
	file_name_val = str(request.POST['file_name_val'])
	print (file_name_val)
	new_object = file(file_name = file_name_val, file=request.FILES.get('user_file'))
	new_object.save()
	url = str(new_object.file_id)
	data = {
		"url" : url
	}
	return JsonResponse(data)

def download_file(request, file_id): 
	file_object = file.objects.get(file_id = file_id) 
	url = str(file_object.file.url) 
	context = {
		'url' : url, 
	}
	return render(request, 'html/file.html', context) 