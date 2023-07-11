from validation import Validation

def test_loan_amount_validation():
    # Testing the loan amount validation
    validation = Validation()

    # Test case 1: Valid loan amount
    valid, value = validation.validate_loan_amount("10000")
    assert valid and value == 10000  # Expect True and 10000

    # Test case 2: Invalid loan amount (negative)
    valid, value = validation.validate_loan_amount("-10000")
    assert not valid and value is None  # Expect False and None

    # Test case 3: Invalid loan amount (non-numeric)
    valid, value = validation.validate_loan_amount("abc")
    assert not valid and value is None  # Expect False and None