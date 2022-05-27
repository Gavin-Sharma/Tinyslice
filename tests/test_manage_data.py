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
        ],
        "budget": 69
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
        ],
        "budget": 420
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

@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_get_total_cost(mock_file):
    json_data = manage_data.read()
    assert (manage_data.get_total_cost("list 1")) == 9.0
    assert (manage_data.get_total_cost("list 2")) == 10.0


def test_save_total_cost():
    #writes the fake data to the json file to set up the template I want
    with open("static_files/data.json", "w") as fp:
        data = json.loads(FAKE_DATA)
        json.dump(data, fp)

    #get and saves the total cost
    manage_data.save_total_cost("list 2")

    #reads the json file
    json_data = manage_data.read()

    assert json_data[1]["total_cost"] == 10.0
    

def test_save_budget():
    # write the test data to the file
    with open("static_files/data.json", "w") as fp:
        data = json.loads(FAKE_DATA)
        json.dump(data, fp)
    manage_data.save_budget(420.69, "list 2")
    json_data = manage_data.read()
    assert json_data[1]["budget"] == 420.69

@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_get_all_list_names(mock_file):
    list_names = manage_data.get_all_list_names()
    assert list_names == ['list 1', 'list 2']


@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_get_number_of_lists(mock_file):
    test_data = manage_data.get_number_of_lists()
    assert test_data == 2

def test_total_list_costs():
    pass

@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_total_number_items(mock_file):
    number_of_items = manage_data.total_number_items()
    assert number_of_items == 4

@patch("builtins.open", new_callable=mock_open, read_data=FAKE_DATA)
def test_all_budgets_and_list_names(mock_file):
    lists_and_budgets = manage_data.all_budgets_and_list_names()
    assert lists_and_budgets[0][0] == "list 1"
    assert lists_and_budgets[0][1] == 69
    assert lists_and_budgets[1][0] == "list 2"
    assert lists_and_budgets[1][1] == 420

def test_all_item_costs():
    pass

def test_calculate_mean():
    pass



