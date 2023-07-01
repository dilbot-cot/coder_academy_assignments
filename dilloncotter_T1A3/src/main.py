from input import UserInput
from calculations import Loan

def main():
    user_input = UserInput()

    loan_amount = user_input.get_loan_amount()
    frequency = user_input.get_repayment_frequency()
    term_start, term_end = user_input.get_term_range()
    rate_start, rate_end = user_input.get_interest_rate_range()

    # Map the frequencies to the number of repayments per year
    frequencies = {
        "weekly": 52,
        "fortnightly": 26,
        "monthly": 12
    }

    for term in range(term_start, term_end + 1):
        for rate in range(int(rate_start * 100), int(rate_end * 100) + 1, 25):
            loan_calculator = Loan(loan_amount, frequencies[frequency])
            loan_calculator.loan_term = term
            loan_calculator.interest_rate = rate / 100
            repayments = loan_calculator.calculate_loan_repayments()
            print(f"For a loan term of {term} years and an interest rate of {rate / 100}%, your repayments would be ${repayments:.2f} {frequency}.")

if __name__ == "__main__":
    main()