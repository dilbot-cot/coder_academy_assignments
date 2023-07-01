from input import UserInput
from calculations import Loan

def main():
    # initialises UserInput and Loan in the main package
    user_input = UserInput()
    loan_calculator = Loan()
# get all user inputs
    loan_amount = user_input.get_loan_amount()
    frequency = user_input.get_repayment_frequency()
    term_start, term_end = user_input.get_term_range()
    rate_start, rate_end = user_input.get_interest_rate_range()

    #complete loop over rate and term
    for term in range(term_start, term_end + 1):
        for rate in range(int(rate_start * 100), int(rate_end * 100) + 1, 25):
            repayments = loan_calculator.calculate_loan_repayments(loan_amount, frequency, term, rate / 100)
            print(f"For a loan term of {term} years and an interest rate of {rate / 100}%, your repayments would be ${repayments:.2f} per {frequency}.")