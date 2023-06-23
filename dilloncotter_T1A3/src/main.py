# Define a function that will caluclate loan repayments based off user inputs
# Inputs = Loan Amount (float), Loan Interest (float), Repayment frequency (string), Loan term (integer), Loan start

def calculate_loan_payment(loan_amount, interest_rate, repayment_freq, loan_term):
    # Control to check repayment
    if repayment_freq == "m":
        n = loan_term * 12
    elif repayment_freq == "f":
        n = loan_term * 26
    elif repayment_freq == "w":
        n = loan_term * 52
    else:
        raise ValueError(f"Invalid repayment history selected ({repayment_freq}), please list either w for weekly, f for fortnightly or m for monthly repayments")
