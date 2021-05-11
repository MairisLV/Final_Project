from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, FormView

from Final_App.models import Loans
from Final_App.forms import NewLoanForm
from Final_App.basic_calculation import Calculate_Loan

def get_interest_pmt(amount, term, rate):
    simple_calc = Calculate_Loan(loan_amount=amount, term=term, interest_rate=rate)

    return int(simple_calc.interest())

# Create your views here.
class IndexListView(ListView):
    model = Loans
    template_name = 'IndexView.html'

class DepositDetailView(DetailView):
    model = Loans
    template_name = 'LoanDetails.html'

def RegisterLoan(request):
    
    if request.method == 'POST':

        loan_amount=request.POST["loan_amount"]
        loan_term=request.POST["loan_term"]
        interest_rate=request.POST["interest_rate"]
        
        interest_pmt = get_interest_pmt(
                            amount=loan_amount,
                            term=loan_term,
                            rate=interest_rate)
        
        registered_loan = Loans(
            loan_amount=loan_amount,
            loan_term=loan_term,
            interest_rate=interest_rate,
            interest_pmt=interest_pmt,
         )

        registered_loan.save()

        context = {
            'user_id': registered_loan.id,
            'username': registered_loan.loan_amount,
            'email': registered_loan.loan_term,
            'interest_rate':registered_loan.interest_rate,
            'interest_pmt': registered_loan.interest_pmt

        }

        return render(
            template_name='IndexView.html',
            request=request,
            context=context
            )

    return render(
        template_name='NewLoanView.html',
        request=request,
        context={},
    )


# class NewLoanView(FormView):
#     form_class = NewLoanForm
#     template_name = 'NewLoanView.html'
#     success_url = "/"
    
            
#     def form_valid(self, form):
#         self.object = form.save(commit = False)

#         post_loan_amount = int(self.request.POST['loan_amount'])
#         post_loan_term = int(self.request.POST['loan_term'])
#         post_interest_rate = float(self.request.POST['interest_rate'])

#         interest_pmt = get_interest_pmt(
#                             amount=post_loan_amount,
#                             term=post_loan_term,
#                             rate=post_interest_rate)

#         form_class['interest_pmt'] = interest_pmt
       
#         self.object.save()
        
#         return super().form_valid(form)

#         # Calculate_Loan