from calculations import RepaymentCalculator
from loan_details import LoanDetails

def test_calculate_loan_repayments():
    # Testing with a known loan amount, term and interest rate.
    
    # Test 1: 5 year term with 5% interest
    loan_details_1 = LoanDetails(10000, 12, 5, 5)
    loan_1 = RepaymentCalculator(loan_details_1)
    assert abs(loan_1.calculate_loan_repayments() - 188.71) < 0.01

    # Test 2: 10 year term with 5% interest
    loan_details_2 = LoanDetails(10000, 12, 10, 5)
    loan_2 = RepaymentCalculator(loan_details_2)
    assert abs(loan_2.calculate_loan_repayments() - 106.07) < 0.01