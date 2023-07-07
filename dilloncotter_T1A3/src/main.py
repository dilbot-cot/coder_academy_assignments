from input import UserInput
from calculations import RepaymentCalculator
from validation import Validation
from loan_details import LoanDetails
from data_writer import DataWriter

def main():
    #Use the UserInput class to handle all user inputs.
    user_input = UserInput()

    while True:
        # Get loan amount from user
        loan_amount = user_input.get_loan_amount()
        # Get repayment frequency from user
        frequency = user_input.get_repayment_frequency()
        # Get loan term range from user
        term_start, term_end = user_input.get_term_range()
        #Get interest rate range from user
        rate_start, rate_end = user_input.get_interest_rate_range()

        # Confirm all user inputs
        if user_input.confirm_inputs(loan_amount, frequency, term_start, term_end, rate_start, rate_end):
            break

    # Map the frequencies to the number of repayments per year
    frequencies = {
        "weekly": 52,
        "fortnightly": 26,
        "monthly": 12
    }

    data = [
        ["For a loan of :" , f"${loan_amount}"],
        ["Loan term", "Interest Rate", "Repayments", "Frequency"]
    ]
    
    for term in range(term_start, term_end + 1):
        for rate in range(int(rate_start * 100), int(rate_end * 100) + 1, 25):
            loan_details = LoanDetails(loan_amount, frequencies[frequency], term, rate / 100)
            repayment_calculator = RepaymentCalculator(loan_details)
            repayments = repayment_calculator.calculate_loan_repayments()
            row = [f"{term}y", f"{format(rate / 100, '.2f')}%", f"${format(repayments, ',.2f')}", frequency.capitalize()]
            data.append(row)
            print(f"For a loan term of {term} years and an interest rate of {format(rate / 100, '.2f')}%, your repayments would be ${format(repayments, ',.2f')} {frequency}.")

    DataWriter.write_csv('loan_data.csv', data)

# Call the main function
if __name__ == "__main__":
    main()