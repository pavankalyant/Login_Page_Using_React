
from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

client = MongoClient()
db = client['React_traial']
coll = db['login_credentials']

@app.route('/sample', methods=["POST"])
def sample():
    email = request.json.get('email')
    password = request.json.get('password')
    if email and password:
        coll.insert_one({'email': email, 'password': password})
        return jsonify({"message": "Inserted Successfully...!!!!!!"})
    else:
        return jsonify({"message": "Failed to insert"}), 400

if __name__ == '__main__':
    app.run(debug=True)

