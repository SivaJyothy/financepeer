from django.shortcuts import render
from task.models import *
from django.http import HttpResponse
import json



# Create your views here.
def login(request):
	if request.method=='POST':
		name=request.POST['username']
		pwd = request.POST['password']

		# data = user(user_name=name, password =pwd)
		# data.save()
		# return HttpResponse('Success')

		try:
			data = user.objects.get(user_name=name)
		except:
			return HttpResponse("Not a valid user")

		if data.password == pwd:
			return render(request, 'pages/index.html', {'message': 0})

	return render(request, 'pages/login.html')

def index(request):
	if request.method =='POST':
		data = request.POST['json_text']
		res = json.loads(data)
		d = user_posts.objects.all().delete()
		
		for i in res:
			data = user_posts(userId=i['userId'], postId=i['id'], title=i['title'], body=i['body'])
			data.save()


		return render(request, 'pages/index.html', {'message': 1})
	return render(request, 'pages/index.html', {'message': 0})



def fun(request):
	data=user_posts.objects.all()
	return render(request, 'pages/posts.html',{'info':data})