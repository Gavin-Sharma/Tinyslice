from unicodedata import name
from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from manage_data import to_dict, read, save, save_total_cost, delete_list, delete_item

# initialize the Flask application
app = Flask(__name__, static_folder="static_files")
nav = Nav(app)

#Control Navigation Bar
nav.register_element('my_navbar', Navbar(
    'thenav',
    View('Home', 'homepage'),
    View('Contact us', 'contact'),
    View('Add Grocery', 'grocery')))


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/grocery", methods = ["POST", "GET"])
def grocery():
    """This page allows users to only add things to a grocery list"""
    if request.method == "POST":
        list_name_data = request.form["listName"] #get list name from form
        item_name_data = request.form["itemName"] #get item name from form
        item_price_data = request.form["itemPrice"] #get item price from form

        #process to save data
        formated_data = to_dict(list_name_data, item_name_data, item_price_data) #formats data
        save_data = save(formated_data, list_name_data, item_name_data, item_price_data) #saves data by creating or appending to a list
        save_total_list_cost = save_total_cost(list_name_data) #saves total cost of each list

        #process to show data
        json_data = read()

        
        return render_template("grocery.html", grocery_lists = json_data)
    return render_template("grocery.html")

@app.route("/delete", methods = ["POST"])
def delete():
    json_data = delete_list(list(request.form.to_dict())[0])
    return render_template("grocery.html", grocery_lists = json_data)

@app.route("/remove", methods = ["POST"])
def remove():

    data_retrieved = []
    # both the list item and list name are returned as a string in the first index of the list
    # the list is turned into a string and the split method is used to separate the item and list name
    form_data = str(list(request.form.to_dict())[0])

    # since the retireved data is in a string form, I am removing all the characters that are not part of the grocery name
    # after removing the characters, I converted it to a list and grabbed the grocery list name and the grocery name
    form_data_one = form_data.replace(",", "")
    form_data_two = form_data_one.replace("[", "")
    form_data_three = form_data_two.replace("]", "")
    form_data_four = form_data_three.replace("'", "")
    form_data_list = form_data_four.split(' ')
    list_item = form_data_list[0]
    list_name = form_data_list[2]

    json_data = delete_item(list_name, list_item)
    return render_template("grocery.html", grocery_lists = json_data)

@app.route("/contact")
def contact():
    """Renders the contact page"""
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
