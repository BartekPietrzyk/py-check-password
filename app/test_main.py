from .main import check_password


def test_should_check_min_length() -> None:
    assert check_password("qwert") is False


def test_should_check_upper_letter() -> None:
    assert check_password("pass@word1") is False


def test_should_check_max_length() -> None:
    assert check_password("Pass@word123456789098765") is False


def test_should_check_digit() -> None:
    assert check_password("passW@ord") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Password1") is False
