import json
import statistics



def to_dict(list_name, item_name, item_price):
    """ This funtion just formats the data before it should be written into the json file """
    return  {
            "list_name": list_name,
            "total_cost": 0,
            "budget": 0,
            "grocery":[[item_name, float(item_price)]]
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
            i["grocery"].append([item_name, float(item_price)])
        
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
    with open("static_files/data.json", "r") as fp:
        # load the data as a python object
        json_data = json.load(fp)
        # loop through the list
        for grocery_list in json_data:
            # if the name of the grocery list matches the name given as the function parameter, delete the grocery list
            if grocery_list["list_name"] == name:
                json_data.remove(grocery_list)

    with open("static_files/data.json", "w") as fp:
        # this would save the data to the file
        json.dump(json_data, fp)
    #returns the data
    return json_data

def delete_item(grocery_list, item):
    """Deletes grocery items from grocery list.
    The grocery_list arugment is from which grocery list to delete the item from.
    The item argument is what item to delete from the gorcery list."""

    with open("static_files/data.json", "r") as fp:
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

    with open("static_files/data.json", "w") as fp:
        # this will save the data
        json.dump(json_data, fp)

    # return the data
    return json_data

def get_all_list_names():
    """Gets all the list names from the data.json file and returns a list"""
    
    json_data = read() #read data
    list_names = [data["list_name"] for data in json_data] #List Comprehension (appends list names into the list->[])
    return list_names

def list_name_and_total_cost():
    """reutrns a list of all the grocery list names and item costs"""
    list_names = get_all_list_names()

    list_name_and_cost = {'List Name' : 'Total Cost'} #notice i have a key and value dont remove it. Google charts does not like when it is removed
    for list_name in list_names:
        total_list_cost = get_total_cost(list_name)
        list_name_and_cost[list_name] = total_list_cost
        

    return list_name_and_cost

def get_number_of_lists():
    """
    gets all the list names using the get_all_list_names funtion and returns the length
    of the number of list names
    """
    list_names = get_all_list_names()
    return len(list_names)

def total_list_costs():
    """
    calculates total item costs for all lists you have
    in the data_json file and returns the float value e.g 43.0
    """
    list_names = get_all_list_names()
    
    total_cost = 0 #track total cost
    for list_name in list_names:
        single_list_cost = get_total_cost(list_name) 
        total_cost += single_list_cost
    return total_cost

def total_number_items():
    """In every list this funtion will get the total number of items a user wants to buy"""

    json_data = read()

    number_of_items = 0 #track number of items in the lists 
    for data in json_data:
        number_of_items += len(data["grocery"])
    return number_of_items

def all_budgets_and_list_names():
    """Gets all the list names and budgets and returns a list [[l1, 5]]"""
    
    json_data = read() #read data
    budget_and_list_name = [[data["list_name"], data["budget"]] for data in json_data]
    return budget_and_list_name

def all_item_costs():
    """gets all items cost in each list and returns a list of item costs"""

    json_data = read()

    item_costs = [] #track all item costs
    for data in json_data:
        for grocery_item in data["grocery"]:
            item_costs.append(grocery_item[1]) #appends the grocery item cost
    
    return item_costs
    
def calculate_mean():
    """gets the stats mean/avg of all the item costs in the grocery lists"""
    data = all_item_costs()
    if len(data) == 0: 
        data = [0]

    return "{:.5f}".format(statistics.mean(data))


def save_budget(budget: float, list_name:str):
    if budget == "":
        budget = 0.0
        
    with open("static_files/data.json") as fp:
        json_data = json.load(fp)

    for grocery_list in json_data:
        if grocery_list["list_name"] == list_name:
            grocery_list.update({"budget": float(budget)})
            break
    
    with open("static_files/data.json", "w") as fp:
        json.dump(json_data, fp)    


def main():
    pass
if __name__ =="__main__":
    main()