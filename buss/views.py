from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def home(request):
	return render(request, 'buss/homePage.html')

def form(request):
	form = PassengerForm()

	if request.method == 'POST':
		form = PassengerForm(request.POST)
		if form.is_valid():
			form.save()
			id = request.POST.get("id")
			return redirect('/payment/')
					
	context = {'form': form}

	return render(request, 'buss/form.html', context)

def payment(request):
	return render(request, 'buss/payment.html')


def messages(request):
	current_user = Passenger.objects.latest("id")
	print(current_user.id)
	context = {'current_user': current_user}
	return render(request, 'buss/messages.html', context)
					

def download(request):
	if request.method == 'POST':
		id = request.POST.get("id")
		print(id)
		passenger = Passenger.objects.get(id=id)
		print(passenger)
		return render(request, 'buss/downloadTicket.html', {'passenger': passenger})
	else:
		return HttpResponse("Not found")


def rate(request):
	return render(request, 'buss/rates.html')

def contact(request):
	return render(request, 'buss/contact.html')							