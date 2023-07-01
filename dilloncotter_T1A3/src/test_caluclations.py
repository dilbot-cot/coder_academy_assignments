from calculations import Loan

def test_loan_repayments():
    #Testing with a known loan amount and term.
    loan = Loan(10000, 12)

    #conduct tests
    # using abs and <0.01 allows for rounding issues commonplace with using interest rates
    assert abs(loan.calculate_loan_repayments(5, 5) - 188.71) < 0.01 #5y loan term, 5% interest
    assert abs(loan.calculate_loan_repayments(10,5) - 106.07) < 0.01 #10y loan term, 5% interest