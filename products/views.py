from django.shortcuts import render

def home(request):
	# if request.user.is_authenticated():
	# 	context={'username':request.user}
	# else:
	# 	context={'username':'Anonymous'}
	context={'username':request.user}
	return render(request,'products/home.html',context)
# Create your views here.
