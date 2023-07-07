class RepaymentCalculator:
    # Initialise loan with loan details
    def __init__(self, loan_details):
        self.loan_details = loan_details

    #Function to calculate the repayments for a loan.
    def calculate_loan_repayments(self):
        #Calculate the interest rate per repayment period (Done by dividing annual interest rate by the number of payments per year)
        rate = self.loan_details.interest_rate / (100 * self.loan_details.num_payments)
        #Total repayments for the loan term.
        repayments = self.loan_details.loan_term * self.loan_details.num_payments
        # Calculate the repayment amount for the loan.
        # The formula takes into account the interest rate per repayment period
        # and the total number of repayments over the loan term.
        return (rate * self.loan_details.loan_amount) / (1 - (1 + rate) ** -repayments)