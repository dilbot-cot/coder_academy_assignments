class Loan:
    # Initialise loan with an amount and the number of repayments
    def __init__(self, loan_amount, num_payments):
        self.loan_amount = loan_amount
        self.num_payments = num_payments

    # Calculates and returns the laon repayment for a specific loan term and interest rate
    def calculate_loan_repayments(self, loan_term, interest_rate):
        rate = (interest_rate / 100) / 12 #interest is charged monthly
        repayments = loan_term * self.num_payments
        return (rate * self.loan_amount) / (1 - (1 + rate) ** -repayments)