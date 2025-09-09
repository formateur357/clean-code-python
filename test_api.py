from unittest.mock import patch

@patch("src.weqther.requests.get")
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {"temp": 25}

    from api import get_weather
    result = get_weather("Paris")

    assert result == 25
    mock_get.assert_called_once()