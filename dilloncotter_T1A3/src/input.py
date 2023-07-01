class UserInput:
    # Function to get the loan amount from user
    def get_loan_amount(self):
        while True:
            try:
                #Ask for the loan amount
                loan_amount = float(input("Please enter the loan amount: $"))
                if loan_amount > 0:
                    return loan_amount
                else:
                    print("Loan amount must be a positive number. Please try again.")
            except ValueError: #handles error where a non numerical value is input
                print("Invalid input. Please enter a number.")

    #function to get the repayment frequency
    def get_repayment_frequency(self):
        while True:
            print("[1] - Weekly repayments")
            print("[2] - Fortnightly repayments")
            print("[3] - Monthly repayments")
            try:
                frequency = int(input("Enter repayment frequency (1, 2, or 3): "))
                if frequency == 1:
                    return "weekly"
                elif frequency == 2:
                    return "fortnightly"
                elif frequency == 3:
                    return "monthly"
                else:
                    print("Invalid selection. Please enter either 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.") #handles error where a non numerical value is input

    # function to get the loan term range
    def get_term_range(self):
        while True:
            try:
                #ask for the loan term range
                term_start = int(input("Enter the start of the loan term you would like to test (in years): "))
                term_end = int(input("Enter the end of the loan term you would like to test (in years): "))
                if term_start > 0 and term_end > 0 and term_end >= term_start:
                    return term_start, term_end
                else:
                    print("Inavlid range. Both terms must be positive and term end must be larger or equal to term start")
            except ValueError:
                print("Invalid input. Please enter a number.") #handles error where a non numerical value is input