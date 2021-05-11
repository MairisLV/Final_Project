from django.db import models

# Create your models here.
class Loans(models.Model):
    loan_amount = models.IntegerField()
    loan_term = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=2, decimal_places=2)
    interest_pmt = models.DecimalField(max_digits=5, decimal_places=2)