from calculations import Loan

def test_loan_repayments():
    # Testing with a known loan amount, term and interest rate.
    
    # Test 1: 5 year term with 5% interest
    loan_1 = Loan(10000, 12)
    loan_1.loan_term = 5
    loan_1.interest_rate = 5
    assert abs(loan_1.calculate_loan_repayments() - 188.71) < 0.01

    # Test 2: 10 year term with 5% interest
    loan_2 = Loan(10000, 12)
    loan_2.loan_term = 10
    loan_2.interest_rate = 5
    assert abs(loan_2.calculate_loan_repayments() - 106.07) < 0.01