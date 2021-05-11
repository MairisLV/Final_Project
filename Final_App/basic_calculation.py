class Calculate_Loan():
    
    def __init__(self, loan_amount, term, interest_rate):
        self.loan_amount = loan_amount
        self.term = term
        self.interest_rate = interest_rate
    
    def interest(self):
        # S=K(1+i)^n
        
        for period in range(int(self.term)):
            total = float(self.loan_amount) * float((1+float(self.interest_rate))**float(period+1))
            
        total = total - int(self.loan_amount)
        return  total
        
