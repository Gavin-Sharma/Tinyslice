import json

class Manage_Data():
    def __init__(self):
        pass

    def to_dict(self, list_name, item_name, item_price):
        """ This funtion just formats the data before it should be written into the json file """
        return {"list_name": list_name,
                "item_name": item_name,
                "item_price": item_price
               }
    
    def save(self, data):
        """ 
        This function should just save the data to a json file with a correct format so make sure to run to_dict funtion first than
        pass the to_dict return variable into the save(data) as an argument. The json data should be a list [] 
        """

        #reads the whole json file and appends it into a list called json_data
        with open("static_files/data.json") as f:
            json_data = json.load(f)
            json_data.append(data)
        
        #after read the json data above, this will append the data you want to data in the format you want. 
        with open("static_files/data.json", "w") as f:
            json.dump(json_data, f)
    
    def read(self):
        with open("static_files/data.json") as f:
            json_data = json.load(f)
            return json_data
    
    def get_list_names(self):
        """"""
        #reads the json file
        with open("static_files/data.json") as f:
            json_data = json.load(f)
        
        #gets only the list names and appends to a list
        data_list_names = []
        for data in json_data:
            data_list_names.append(data["list_name"])
        
        return data_list_names 





def main():
    x = Manage_Data()
    x.save({'list_name': 'gavinlist', 'item_name': 'pizza', 'item_price': '1'})

if __name__ =="__main__":
    main()