class Loan:
    # Initialise loan with an amount and the number of repayments
    def __init__(self, loan_amount, num_payments):
        self.loan_amount = loan_amount
        self.num_payments = num_payments

    def calculate_loan_repayments(self):
        rate = self.interest_rate / (100 * self.num_payments) #interest is charged per repayment period
        repayments = self.loan_term * self.num_payments
        return (rate * self.loan_amount) / (1 - (1 + rate) ** -repayments)