from django.forms import ModelForm
from .models import Passenger


class PassengerForm(ModelForm):
	class Meta:
		model = Passenger
		fields = '__all__'