from services import UserService
from unittest.mock import MagicMock, patch

def test_register_user_sends_notification():
    mock_notifier = MagicMock()
    mock_notifier.send.return_value = True

    service = UserService(mock_notifier)
    result = service.register_user("test@mail.com")

    assert result is True

    mock_notifier.send.assert_called_once_with("test@mail.com", "Welcome!")

@patch("services.NotificationService")
def test_register_user_with_patch(mock_notifier):
    mock_instance = mock_notifier.return_value
    mock_instance.send.return_value = True

    service = UserService(mock_instance)
    service.register_user("patch@test.com")

    mock_instance.send.assert_called_once()