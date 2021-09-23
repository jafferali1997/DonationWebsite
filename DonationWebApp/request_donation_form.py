from django import forms
from .models import RequestForDonation

class RequestDonationForm(forms.ModelForm):
    class Meta():
        model = RequestForDonation
        fields = ('Name','Purpose','CNIC','Address','Description','Contact_Number','Email')