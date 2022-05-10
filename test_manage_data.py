from unittest.mock import mock_open, patch
import manage_data

FAKE_DATA = """[
    {
        "list_name": "list 1",
        "grocery": [
            [
                "apples",
                "5"
            ],
            [
                "pears",
                "4"
            ]
        ]
    }
]"""

@patch("builtins.open", new_callable=mock_open, read_data = FAKE_DATA)
def test_read(mock_file):
    json_data = manage_data.read()
    assert json_data[0]["list_name"] == "list 1"
    assert json_data[0]["grocery"][0][0] == "apples"