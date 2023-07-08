class Validation:
    #Function to validate the loan amount
    #This is used for testing
    @staticmethod
    #staticmethod allows us to call the validate_loan_amount function without creating it as an object
    def validate_loan_amount(loan_amount):
        try:
            loan_amount = float(loan_amount)
            if loan_amount > 0:
                return True, loan_amount
            else:
                return False, None
        except ValueError:
            return False, None