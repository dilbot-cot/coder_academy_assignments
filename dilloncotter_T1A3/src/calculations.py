class Loan:
    # Initialise loan with an amount and the number of repayments
    def __init__(self, loan_amount, num_payments):
        self.loan_amount = loan_amount #The total amount of the loan
        self.num_payments = num_payments #The total number of repayments to be made.

    #Function to calculate the repayments for a loan.
    def calculate_loan_repayments(self):
        #Calculate the interest rate per repayment period (Done by dividing annual interest rate by the number of payments per year)
        rate = self.interest_rate / (100 * self.num_payments)

        #Total repayments for the loan term.
        repayments = self.loan_term * self.num_payments

        # Calculate the repayment amount for the loan.
        # The formula takes into account the interest rate per repayment period
        # and the total number of repayments over the loan term.
        return (rate * self.loan_amount) / (1 - (1 + rate) ** -repayments)