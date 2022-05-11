import json



def to_dict(list_name, item_name, item_price):
    """ This funtion just formats the data before it should be written into the json file """
    return  {
            "list_name": list_name,
            "total_cost": 0,
            "grocery":[[item_name, int(item_price)]]
            }

def read():
    """Reads the json file and return the read file"""
    with open("static_files/data.json") as f:
        json_data = json.load(f)
        return json_data
    
def get_total_cost(list_name):
    """Takes a list name you want to get the total cost for and returns the total cost"""
    #read the json file and store in variable
    json_data = read()

    for data in json_data:
        if data["list_name"] == list_name:

            #keep track of the total cost
            total_cost = 0

            for item_cost in data["grocery"]:
                total_cost += item_cost[1] #adds item cost to total_cost
            
            #return the total cost for the list
            return total_cost

def save_total_cost(list_name):
    """saves the total cost of a grocery list using the get_total_cost funtion"""
    json_data = read() #read data
    total_cost = get_total_cost(list_name) #get total cost for a single list

    #Check if list name match and change the total_cost value in the json_data
    for data in json_data:
        if data["list_name"] == list_name:
            data["total_cost"] = total_cost #update the total cost to json_data
    
    #Writes to the json file
    with open("static_files/data.json", "w") as f:
        json.dump(json_data, f)


def save(data, list_name, item_name, item_price):
    #Reads json file
    json_data = read()

    #Keep track of all the list names
    all_list_names = []

    #Appends data to existing list
    for i in json_data:
        if i["list_name"] == list_name:
            i["grocery"].append([item_name, int(item_price)])
        
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

def delete_item(grocery_list, item):
    """Deletes grocery items from grocery list.
    The grocery_list arugment is from which grocery list to delete the item from.
    The item argument is what item to delete from the gorcery list."""
    # open data.json
    with open("static_files/data.json") as fp:
        # load the json as a python object
        json_data = json.load(fp)
        # find the index of the grocery list that matches the name of the grocery list
        index = next((index for (index, d) in enumerate(json_data) if d["list_name"] == grocery_list), None)
        # loop through the grocery items in the grocery list
        # the grocery list is accessed using the index found above
        for groceries in json_data[index]["grocery"]:
            # if the grocery item matches the item argument, remove the grocery item from the groceries list
            if groceries[0] == item:
                json_data[index]["grocery"].remove(groceries)
                
        # this will save the data
        # json.dump(json_data, fp)

        # return the data
        return json_data




            


def main():
    x = get_total_cost("list2")
    print(x)

if __name__ =="__main__":
    main()