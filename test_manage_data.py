from unittest.mock import mock_open, patch
import manage_data
import json

#fake json, his is a json string
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
    },
    {
        "list_name": "list 2",
        "grocery": [
            [
                "bananas",
                "7"
            ],
            [
                "oranges",
                "3"
            ]
        ]
    }
        
]"""

# opens the fake json as if it were a real file
@patch("builtins.open", new_callable=mock_open, read_data = FAKE_DATA)
def test_read(mock_file):
    # call the function, it opens the fake json instead of the actual file
    # read function returns the json data as a python dictionary
    json_data = manage_data.read()
    assert json_data[0]["list_name"] == "list 1"
    assert json_data[0]["grocery"][0][0] == "apples"
    assert json_data[0]["grocery"][0][1] == "5"
    assert json_data[0]["grocery"][1][0] == "pears"
    assert json_data[0]["grocery"][1][1] == "4"

@patch("builtins.open", new_callable=mock_open, read_data = FAKE_DATA)
def test_delete_list(mock_file):
    json_data = manage_data.delete_list("list 1")
    for grocery_list in json_data:
        assert grocery_list["list_name"] != "list 1"
    assert json_data[0]["list_name"] == "list 2"

@patch("builtins.open", new_callable=mock_open, read_data = FAKE_DATA)
def test_delete_item(mock_file):
    json_data = manage_data.delete_item("list 1", "apples")
    index = next((index for (index, d) in enumerate(json_data) if d["list_name"] == "list 1"), None)
    grocery_list = json_data[index]
    for groceries in grocery_list:
        assert groceries[0] != "apples"