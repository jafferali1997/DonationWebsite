from django import forms
from .models import Donation

class DonationGivingForm(forms.ModelForm):
    class Meta():
        model = Donation
        fields = '__all__'