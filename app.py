from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator
from manage_data import Manage_Data

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

        #insitince of Manage_Data class
        manage_data = Manage_Data()

        #process to save data
        formated_data = manage_data.to_dict(list_name_data, item_name_data, item_price_data) #formats data
        save_data = manage_data.save(formated_data, list_name_data, item_name_data, item_price_data)

        #process to show data
        json_data = manage_data.read()

        
        return render_template("grocery.html", grocery_lists = json_data)
    return render_template("grocery.html")

@app.route("/contact")
def contact():
    """Renders the contact page"""
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
