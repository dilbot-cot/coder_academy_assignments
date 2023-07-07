class Validation:
    @staticmethod
    def validate_loan_amount(loan_amount):
        try:
            loan_amount = float(loan_amount)
            if loan_amount > 0:
                return True, loan_amount
            else:
                return False, None
        except ValueError:
            return False, None