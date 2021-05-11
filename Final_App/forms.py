from django.forms import ModelForm
from Final_App.models import Loans

class NewLoanForm(ModelForm):
    class Meta:
        model = Loans
        fields = ['loan_amount', 'loan_term', 'interest_rate']
        