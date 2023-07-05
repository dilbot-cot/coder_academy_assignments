from input import UserInput

def test_loan_amount_validation():
    # Testing the loan amount validation
    user_input = UserInput()

    # Test case 1: Valid loan amount
    valid, value = user_input.validate_loan_amount("10000")
    assert valid and value == 10000  # Expect True and 10000

    # Test case 2: Invalid loan amount (negative)
    valid, value = user_input.validate_loan_amount("-10000")
    assert not valid and value is None  # Expect False and None

    # Test case 3: Invalid loan amount (non-numeric)
    valid, value = user_input.validate_loan_amount("abc")
    assert not valid and value is None  # Expect False and None