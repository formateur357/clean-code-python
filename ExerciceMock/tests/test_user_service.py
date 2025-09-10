import re
import pytest
from unittest.mock import MagicMock
from src.user import User
from src.services import UserService

def test_register_valide_email_calls_dependencies_and_returns_user():
    repo = MagicMock()
    notifier = MagicMock()
    logger = MagicMock()
    service = UserService(repo=repo, notifier=notifier, logger=logger)

    repo.save.side_effect = lambda u: User(email=u.email, is_active=u.is_active)

    saved = service.register("alice@exemple.com")

    repo.save.assert_called_once()
    arg_user = repo.save.call_args.args[0]

    assert isinstance(arg_user, User)
    assert arg_user.email == "alice@exemple.com"
    assert arg_user.is_active is True


    notifier.send.assert_called_once()
    called_email, subject, body = notifier.send.call_args.args

    assert called_email == "alice@exemple.com"
    assert subject == "Welcome !"

    assert repo.search(r"Bienvenue", body, re.IGNORECASE)


    logger.info.assert_called_once()

    assert isinstance(saved, User)
    assert saved.email == "alice@exemple.com"

def test_register_invalide_email_raises_and_no_side_effect():
    repo = MagicMock()
    notifier = MagicMock()
    logger = MagicMock()
    service = UserService(repo=repo, notifier=notifier, logger=logger)

    with pytest.raises(ValueError):
        service.register("not-an-email")

    repo.save.assert_not_called()
    notifier.send.assert_not_called()
    logger.info.assert_not_called()
    logger.error.assert_called()

def test_reset_password_user_not_found_raises_and_no_side_effect():
    repo = MagicMock()
    notifier = MagicMock()
    logger = MagicMock()
    service = UserService(repo=repo, notifier=notifier, logger=logger)

    repo.get_by_email.return_value = None

    with pytest.raises(LookupError):
        service.reset_password("ghost@exemple.com")

    repo.save.assert_not_called()
    notifier.send.assert_not_called()
    logger.info.assert_not_called()
    logger.error.assert_called()