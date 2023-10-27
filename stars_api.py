from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data" : data
    })

@app.route("/star")
def planet():
    name = request.args.get("star_name")
    star_data = next(item for item in data if item["star_name"] == name)

    return jsonify({
        "data" : star_data
    }),200

# Link to view the data for individual star: http://127.0.0.1:5000/star?star_name=____

if __name__ == "__main__":
    app.run()
