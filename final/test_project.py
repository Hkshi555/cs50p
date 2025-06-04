from project import check_length, check_uppercase, check_lowercase, \
                   check_digits, check_special_chars, check_common_words, \
                   calc_pass_score, generate_password

def test_check_length():
    assert check_length("short", min_length=8) == False
    assert check_length("longenough", min_length=8) == True
    assert check_length("1234567", min_length=8) == False
    assert check_length("12345678", min_length=8) == True

def test_check_uppercase():
    assert check_uppercase("abc") == False
    assert check_uppercase("Abc") == True
    assert check_uppercase("ABC") == True

def test_check_lowercase():
    assert check_lowercase("ABC") == False
    assert check_lowercase("ABc") == True
    assert check_lowercase("abc") == True

def test_check_digits():
    assert check_digits("abc") == False
    assert check_digits("abc1") == True
    assert check_digits("123") == True

def test_check_special_chars():
    assert check_special_chars("abc") == False
    assert check_special_chars("abc!") == True
    assert check_special_chars("!@#") == True

def test_check_common_words():
    assert check_common_words("password") == True
    assert check_common_words("MyP@ssword") == False
    assert check_common_words("MySecret") == True

def test_calc_pass_score():
    # Test a clearly low strength password (too short)
    strength, feedback, score = calc_pass_score("short")
    assert strength == "Low Strength Password"
    assert "Password should be at least 8 characters long." in feedback
    assert score == 1

    # Test a password containing a common word (should be critical failure)
    strength, feedback, score = calc_pass_score("password123")
    assert strength == "Low Strength Password"
    assert "Password contains common or easily guessable words. Avoid common words!" in feedback
    assert score == 3

    # Password that is long enough but lacks variety
    strength, feedback, score = calc_pass_score("longenoughpassword123")
    assert strength == "Medium Strength Password" # Expected to be Medium due to length but missing types
    assert "Password should contain at least one uppercase letter." in feedback
    assert "Password should contain at least one special character." in feedback
    assert "Password should contain at least one lowercase letter." not in feedback # Should have lowercase
    assert "Password should contain at least one digit." not in feedback # Should have digits
    # Score should be based on: Length (1) + Lowercase (1) + Digits (1) + Bonus for >12 chars (1) = 4
    # Expected score based on our calc_pass_score logic: 1 (length) + 1 (lowercase) + 1 (digits) + 1 (>=12 length) = 4.
    # So 4 is a medium score.
    assert score == 5


    # Test a medium strength password
    strength, feedback, score = calc_pass_score("mediumP1!")
    assert strength == "Medium Strength Password"
    assert score >= 4 and score <= 6 # Should meet most criteria
    assert not feedback # Should have no feedback (as it met all basic requirements)

    # Test a high strength password
    strength, feedback, score = calc_pass_score("StrongP@ssw0rd123!")
    assert strength == "High Strength Password"
    assert score >= 7 # Should meet all criteria and bonuses
    assert not feedback # Should have no feedback

def test_generate_password():

    gen_pass_default = generate_password()
    assert len(gen_pass_default) == 12

    assert check_uppercase(gen_pass_default)
    assert check_lowercase(gen_pass_default)
    assert check_digits(gen_pass_default)
    assert check_special_chars(gen_pass_default)

    # Test custom length
    gen_pass_custom_len = generate_password(length=15)
    assert len(gen_pass_custom_len) == 15

    # Test with specific character types disabled
    gen_pass_no_special = generate_password(use_special=False, length=10)
    assert len(gen_pass_no_special) == 10
    assert not check_special_chars(gen_pass_no_special)

    gen_pass_only_lower_digit = generate_password(use_uppercase=False, use_special=False, length=10)
    assert len(gen_pass_only_lower_digit) == 10
    assert check_lowercase(gen_pass_only_lower_digit)
    assert check_digits(gen_pass_only_lower_digit)
    assert not check_uppercase(gen_pass_only_lower_digit)
    assert not check_special_chars(gen_pass_only_lower_digit)
