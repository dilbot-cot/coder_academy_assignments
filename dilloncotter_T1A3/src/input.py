import os

class UserInput:
    # Function to clear terminal
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    # Function to confirm loan details with the user
    def confirm_inputs(self, loan_amount, frequency, term_start, term_end, rate_start, rate_end):
        self.clear_terminal()
        print("Please confirm the following details:")
        print(f"Loan Amount: ${format(loan_amount, ',.2f')}")
        print(f"Repayment frequency: {frequency.capitalize()}")
        print(f"Loan term range: {term_start} years to {term_end} years")
        print(f"Interest rate range: {format(rate_start, '.2f')}% to {format(rate_end, '.2f')}%")
        while True:
            # Get confirmation from the user
            confirmation = self.get_input("Is this information correct (y/n): ")
            if confirmation.lower() == "y":
                return True
            elif confirmation.lower() == "n":
                return False
            else:
                print("Invalid input. Please enter only y or n.")

    # Function to get any user input with the option to exit program
    def get_input(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.lower() == 'exit':
                if self.confirm_exit("Are you sure you wish to exit?"):
                    print("Program stopped at user request.")
                    exit()
                else:
                    continue
            return user_input

    #Function to get the loan amount from the user
    def get_loan_amount(self):
        self.clear_terminal()
        while True:
            try:
                loan_amount = self.get_input("Please enter the loan amount (or type 'exit' to stop the program): $")
                loan_amount = float(loan_amount)
                if loan_amount > 0:
                    return loan_amount
                else:
                    print("Loan amount must be a positive number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Function to get the repayment frequency from the user
    def get_repayment_frequency(self):
        self.clear_terminal()
        while True:
            print("Select your repayment frequency:")
            print("[1] - Weekly repayments")
            print("[2] - Fortnightly repayments")
            print("[3] - Monthly repayments")
            print("Type 'exit' to quit")
            try:
                frequency = self.get_input("Enter repayment frequency (1, 2, or 3): ")
                frequency = int(frequency)
                if frequency == 1:
                    return "weekly"
                elif frequency == 2:
                    return "fortnightly"
                elif frequency == 3:
                    return "monthly"
                else:
                    print("Invalid selection. Please enter either 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    #Function to get the loan term range from user
    def get_term_range(self):
        self.clear_terminal()
        while True:
            try:
                print("Input the loan term range you are testing, type 'exit' to quit")
                term_start = self.get_input("Enter the start of the loan term you would like to test (in years): ")
                term_end = self.get_input("Enter the end of the loan term you would like to test (in years): ")
                term_start = int(term_start)
                term_end = int(term_end)
                if term_start > 0 and term_end > 0 and term_end >= term_start:
                    return term_start, term_end
                else:
                    print("Invalid range. Both terms must be positive, and term end must be larger or equal to term start.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Function to get the interest rate range from the user
    def get_interest_rate_range(self):
        self.clear_terminal()
        while True:
            try:
                print("Input the interest rate range you are testing, type 'exit' to quit")
                rate_start = self.get_input("Enter the start of the interest rate you would like to test: ")
                rate_end = self.get_input("Enter the end of the interest rate you would like to test: ")
                rate_start = float(rate_start)
                rate_end = float(rate_end)
                if rate_start > 0 and rate_end > 0 and rate_end >= rate_start:
                    return rate_start, rate_end
                else:
                    print("Invalid range. Both terms must be positive, and end rate must be larger or equal to start rate.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Function to confirm user's request to exit the program
    def confirm_exit(self, prompt):
        while True:
            confirmation = self.get_input(prompt + " (y/n): ")
            if confirmation.lower() == "y":
                return True
            elif confirmation.lower() == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    #Function to validate the loan amount
    #This is used for testing
    def validate_loan_amount(self, loan_amount):
        try:
            loan_amount = float(loan_amount)
            if loan_amount > 0:
                return True, loan_amount
            else:
                return False, None
        except ValueError:
            return False, None
