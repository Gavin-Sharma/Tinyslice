from flask import Flask, request, jsonify, render_template
#initialize the Flask application
app = Flask(__name__, static_folder="static_files")

# when the app receives a request it returns a html file and a http status code
@app.route("/")
def homepage():
    return render_template("index.html"), 200

if __name__ == "__main__":
    app.run(debug=True)