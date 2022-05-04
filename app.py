import json
from flask import Flask, request, jsonify, render_template
#initialize the Flask application
app = Flask(__name__, static_folder="static_files")

# when the app receives a request at the "/" endpoint, it will activate this function
@app.route("/")
def homepage():
    """Renders the main page"""
    # renders the index.html file and sends the 200 OK HTTP status code
    return render_template("index.html"), 200

# this route only works with GET requests
# later we will copy this route but with the POST method to add items to the list
# we can also use PATCH request to edit the list
@app.route("/api/grocery_list", methods = ["GET"])
def return_grocery_list():
    """Returns a json of the grocery objects stored in the server"""
    # opens the grocery list json file in a read-only state
    with open("grocery_list.json", "r") as fp:
        data = json.load(fp)
    # from jsonify intellisense: Serialize data to JSON and wrap it in a ~flask.Response with the application/json mimetype
    return jsonify(data), 200

if __name__ == "__main__":
    # debug must be set to false in production
    app.run(debug=True)