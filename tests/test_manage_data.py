from unittest.mock import mock_open, patch
import manage_data
import json
import pytest


# fake json, his is a json string
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


@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_read(mock_file):
    # call the function, it opens the fake json instead of the actual file
    # read function returns the json data as a python dictionary
    json_data = manage_data.read()
    assert json_data[0]["list_name"] == "list 1"
    assert json_data[0]["grocery"][0][0] == "apples"
    assert json_data[0]["grocery"][0][1] == "5"
    assert json_data[0]["grocery"][1][0] == "pears"
    assert json_data[0]["grocery"][1][1] == "4"

def test_delete_list():
    # write the test data to the file
    with open("static_files/data.json", "w") as fp:
        data = json.loads(FAKE_DATA)
        json.dump(data, fp)
    # deletes the grocery list with the name "list 1"
    manage_data.delete_list("list 1")
    # retrieve the data
    json_data = manage_data.read()
    
    # verifies that there is no list called "list 1"
    for grocery_list in json_data:
        assert grocery_list["list_name"] != "list 1"
    # verifies if "list 2" is not deleted
    assert json_data[0]["list_name"] == "list 2"

def test_delete_item():
    # write the test data to the file
    with open("static_files/data.json", "w") as fp:
        data = json.loads(FAKE_DATA)
        json.dump(data, fp)
    # deletes the "apples" item from "list 1"
    manage_data.delete_item("list 1", "apples")
    # retrieve the data
    json_data = manage_data.read()
    
    # obtains the index for the list called "list 1"
    # in our case index is 0
    index = next((index for (index, d) in enumerate(
        json_data) if d["list_name"] == "list 1"), None)
    # access the grocery list at index 0
    grocery_list = json_data[index]
    # verifies if the "apples" item is not included in the list
    for groceries in grocery_list:
        assert groceries[0] != "apples"


@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_save(mock_file):
    manage_data_list = []
    f = open('static_files/data.json', 'w')
    f.write(json.dumps(manage_data_list))
    mock_file.assert_called_once()


def test_to_dict():
    fake_list = manage_data.to_dict("List 1", "Apple", 0.99)
    assert fake_list == {"list_name": "List 1",
                         "total_cost": 0,
                         "budget": 0,
                         "grocery": [["Apple", 0.99]]
                         }


def test_get_total_cost():
    pass


def test_save_total_cost():
    pass

def test_save_budget():
    # write the test data to the file
    with open("static_files/data.json", "w") as fp:
        data = json.loads(FAKE_DATA)
        json.dump(data, fp)
    manage_data.save_budget(420.69, "list 2")
    json_data = manage_data.read()
    assert json_data[1]["budget"] == 420.69

def test_get_all_list_names():
    pass

def test_list_name_and_total_cost():
    pass

def test_get_number_of_lists():
    pass

def test_total_list_costs():
    pass

def test_total_number_items():
    pass

def test_all_budgets_and_list_names():
    pass

def test_all_item_costs():
    pass

def test_calculate_mean():
    pass



