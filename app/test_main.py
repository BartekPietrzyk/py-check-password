from .main import check_password


def test_check_password_is_true() -> None:
    assert check_password("Pass@word1") is True


def test_check_password_is_too_short() -> None:
    assert check_password("qwert") is False


def test_check_password_is_too_long() -> None:
    assert check_password("Pass@word123456789098765") is False
