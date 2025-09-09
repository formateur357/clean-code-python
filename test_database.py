from unittest.mock import MagicMock
from database import UserRepository

def test_create_user_calls_db_save():
    mock_db = MagicMock()
    repo = UserRepository(mock_db)

    repo.create_user({"name": "Morgan"})

    mock_db.save.assert_called_once_with({"name": "Morgan"})