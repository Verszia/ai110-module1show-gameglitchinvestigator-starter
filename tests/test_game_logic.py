from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_hint_direction_for_too_high_and_too_low():
    # Regression test: a guess above the secret should say to go lower,
    # and a guess below the secret should say to go higher.
    high_result = check_guess(60, 50)
    low_result = check_guess(40, 50)

    assert high_result == ("Too High", "📉 Go LOWER!")
    assert low_result == ("Too Low", "📈 Go HIGHER!")
