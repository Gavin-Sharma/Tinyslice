import json



def to_dict(list_name, item_name, item_price):
    """ This funtion just formats the data before it should be written into the json file """
    return  {
            "list_name": list_name,
            "grocery":[[item_name, item_price]]
            }

def read():
    """Reads the json file and return the read file"""
    with open("static_files/data.json") as f:
        json_data = json.load(f)
        return json_data
    
def save(data, list_name, item_name, item_price):
    #Reads json file
    json_data = read()

    #Keep track of all the list names
    all_list_names = []

    #Appends data to existing list
    for i in json_data:
        if i["list_name"] == list_name:
            i["grocery"].append([item_name, item_price])
        
        all_list_names.append(i["list_name"])
        
    #Creates a new list and adds the data
    if list_name not in all_list_names:
        json_data.append(data)
        
    #Writes to the json file
    with open("static_files/data.json", "w") as f:
        json.dump(json_data, f)
    
def delete_list(name):
    """Deletes a grocery list based off the name of the grocery list
    given in the argument"""
    # opens data.json
    with open("static_files/data.json", "w") as fp:
        # load the data as a python object
        json_data = json.load(fp)
        # loop through the list
        for grocery_list in json_data:
            # if the name of the grocery list matches the name given as the function parameter, delete the grocery list
            if grocery_list["list_name"] == name:
                json_data.remove(grocery_list)
        # this would save the data to the file
        # json.dump(json_data, fp)

        #returns the data
        return json_data


def main():
    pass
if __name__ =="__main__":
    main()