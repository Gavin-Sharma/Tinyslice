from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
from manage_data import Manage_Data

# initialize the Flask application
app = Flask(__name__, static_folder="static_files")


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
        save_data = manage_data.save(formated_data)

        #process to show data
        json_data = manage_data.read()
        
        return render_template("grocery.html", data = json_data)




if __name__ == "__main__":
    app.run(debug=True)
